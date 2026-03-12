import copy

class ClinicData:
    doctors_by_specialty = {
        "Dermatology": ["Dr. Ahmed Mohamed", "Dr. Ali Ahmed"],
        "Internal Medicine": ["Dr. Aya Magdy", "Dr. Khaled Mohamed"],
        "Pediatrics": ["Dr. Eman Ahmed", "Dr. Omar Alaa"],
        "Cardiology": ["Dr. Hamed Ghoneim", "Dr. Omar Elmalah"]
    }

    available_times_initial = {
        "Dr. Ahmed Mohamed": ["09:00 AM", "10:00 AM", "11:00 AM"],
        "Dr. Ali Ahmed": ["12:00 PM", "01:00 PM", "02:00 PM"],
        "Dr. Aya Magdy": ["11:00 AM", "12:00 PM", "03:00 PM"],
        "Dr. Khaled Mohamed": ["10:00 AM", "01:00 PM", "04:00 PM"],
        "Dr. Eman Ahmed": ["02:00 PM", "03:00 PM", "04:00 PM"],
        "Dr. Omar Alaa": ["02:30 PM", "04:00 PM"],
        "Dr. Hamed Ghoneim": ["05:00 PM", "06:00 PM"],
        "Dr. Omar Elmalah": ["06:00 PM", "07:00 PM"],
    }

class AppointmentManager:
    def __init__(self):
        self.doctors_by_specialty = copy.deepcopy(ClinicData.doctors_by_specialty)
        self.available_times = copy.deepcopy(ClinicData.available_times_initial)
        self.appointments = []
        self.feedback = []
        self.emergency_logs = []
        self.emergency_active = True 

    def get_specialties(self):
        return list(self.doctors_by_specialty.keys())

    def get_doctors(self, specialty):
        return self.doctors_by_specialty.get(specialty, [])

    def get_available_times(self, doctor):
        return self.available_times.get(doctor, [])

    def book_appointment(self, name, phone, specialty, doctor, time):
        if time not in self.available_times.get(doctor, []):
            return False
        self.available_times[doctor].remove(time)
        self.appointments.append({
            "Name": name, "Phone": phone, "Specialty": specialty, "Doctor": doctor, "Time": time
        })
        return True

    def send_feedback(self, name, text):
        self.feedback.append({"Name": name, "Feedback": text})

    def get_all_appointments(self):
        return self.appointments

    def get_all_feedback(self):
        return self.feedback

    def get_emergency_logs(self):
        return self.emergency_logs

    def add_doctor_time(self, doctor, time):
        if doctor in self.available_times and time not in self.available_times[doctor]:
            self.available_times[doctor].append(time)
            return True
        return False

    def remove_doctor_time(self, doctor, time):
        if doctor in self.available_times and time in self.available_times[doctor]:
            self.available_times[doctor].remove(time)
            return True
        return False

    def request_ambulance(self, name, location):
        log = {"Patient": name, "Location": location, "Status": "Ambulance Sent"}
        self.emergency_logs.append(log)
        return log