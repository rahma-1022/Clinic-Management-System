import streamlit as st
import pandas as pd
from appointment_manager import AppointmentManager

st.set_page_config(page_title="Clinic System", page_icon="🏥", layout="wide")

if "manager" not in st.session_state:
    st.session_state.manager = AppointmentManager()

manager = st.session_state.manager

page = st.sidebar.radio("Navigation", ["Home", "Book Appointment", "My Appointments", "Feedback", "Emergency 🚑", "Admin Panel"])

if page == "Home":
    st.markdown("""
        <div style="background-color:#e3f2fd; padding:50px; border-radius:15px; border-left: 10px solid #1976d2; text-align: center;">
            <h1 style="color:#0d47a1; font-size: 45px;">Welcome to Our Professional Clinic 🏥</h1>
            <p style="font-size:20px; color:#333; margin-top:20px;">
                Your health is our top priority. We provide high-quality medical services 
                with a team of experienced specialists.
            </p>
            <p style="font-size:18px; color:#666;">
                Please use the sidebar to <b>Book an Appointment</b> or access <b>Emergency Services</b>.
            </p>
        </div>
    """, unsafe_allow_html=True)

elif page == "Book Appointment":
    st.title("📅 Book Your Appointment")
    st.info("Please enter your details and choose the suitable specialty and doctor.")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Patient Full Name")
        phone = st.text_input("Phone Number")
    with col2:
        spec_choice = st.selectbox("Select Specialty", manager.get_specialties())
        doc_choice = st.selectbox("Select Doctor", manager.get_doctors(spec_choice))
        available_slots = manager.get_available_times(doc_choice)
    if available_slots:
        time_choice = st.selectbox("Available Slots", available_slots)
        if st.button("Confirm Booking", use_container_width=True):
            if name and phone:
                if manager.book_appointment(name, phone, spec_choice, doc_choice, time_choice):
                    st.success(f"Confirmed with {doc_choice} at {time_choice}.")
                else: st.error("Time slot no longer available.")
            else: st.warning("Please provide name and phone.")
    else: st.error("No available slots for this doctor today.")

elif page == "My Appointments":
    st.title("📋 Appointment Records")
    data = manager.get_all_appointments()
    if data: st.dataframe(pd.DataFrame(data), use_container_width=True)
    else: st.info("No records found.")

elif page == "Feedback":
    st.title("📝 Feedback")
    fname = st.text_input("Name")
    msg = st.text_area("Message")
    if st.button("Submit"):
        if fname and msg:
            manager.send_feedback(fname, msg)
            st.success("Thank you! Your feedback has been saved.")

elif page == "Emergency 🚑":
    st.title("🆘 Emergency Service")
    st.error("🚨 Request an ambulance immediately.")
    e_name = st.text_input("Patient Name")
    loc = st.text_input("Location")
    if st.button("Request Now"):
        if e_name and loc:
            res = manager.request_ambulance(e_name, loc)
            st.success("Ambulance dispatched! Admin has been notified.")
            st.json(res)

elif page == "Admin Panel":
    st.title("🛠 Admin Dashboard")
    password = st.text_input("Enter Admin Password", type="password")
    if password == "123456":
        st.success("Access Granted")
        tab1, tab2, tab3 = st.tabs(["Reports & Logs", "Manage Doctors", "Emergency Requests"])
        
        with tab1:
            st.subheader("All Appointments")
            st.write(pd.DataFrame(manager.get_all_appointments()))
            st.subheader("Feedback Logs")
            st.write(pd.DataFrame(manager.get_all_feedback()))
            
        with tab2:
            st.subheader("Edit Doctor Schedule")
            doc_to_edit = st.selectbox("Select Doctor", list(manager.available_times.keys()))
            new_time = st.text_input("New Slot (e.g. 11:00 PM)")
            col_a, col_b = st.columns(2)
            with col_a:
                if st.button("Add Time Slot"):
                    if manager.add_doctor_time(doc_to_edit, new_time): st.success("Added")
            with col_b:
                if st.button("Remove Time Slot"):
                    if manager.remove_doctor_time(doc_to_edit, new_time): st.success("Removed")
                    
        with tab3:
            st.subheader("Ambulance Dispatch Logs")
            e_logs = manager.get_emergency_logs()
            if e_logs: st.table(pd.DataFrame(e_logs))
            else: st.info("No emergency requests yet.")
            
    elif password != "":
        st.error("Incorrect Password")