import copy
class Doctors:
    
    
    doctor_list={"Dermatology":["Dr.Ahmed mohammed ","Dr.Ali Ahmed ","Dr.Hossam Ali "],
                         "Internal Medicine":["Dr.Aya Magdy ","Dr.Alaa Ahmed ","Dr.Kaled mohammed "],
                         "Pediatrics": ["Dr. Eman Ahmed ", "Dr. Youssef Omar ","Dr.Omar Alaa "],
                         "Cardiology": ["Dr. Omar Ahmad ","Dr. Sara Ahmed ","Dr. Mariam Hassan "]}
    
  
    available_times = {
        "Dr.Ahmed mohammed ": ["10:00 AM", "11:00 AM"],
        "Dr.Ali Ahmed ": ["08:00 AM", "12:00 PM"],
        "Dr.Hossam Ali ": ["03:00 PM", "05:00 PM"],
        
        "Dr.Aya Magdy ": ["09:00 AM", "02:00 PM"],
        "Dr.Alaa Ahmed ": ["11:00 AM", "04:00 PM"],
        "Dr.Kaled mohammed ": ["10:00 AM", "01:00 PM"],
        
        "Dr. Eman Ahmed ": ["01:00 PM", "03:00 PM"],
        "Dr. Youssef Omar ": ["09:30 AM"],
        "Dr.Omar Alaa ": ["02:30 PM", "04:00 PM"],
        
        "Dr. Omar Ahmad ": ["04:00 PM"],
        "Dr. Sara Ahmed ": ["05:00 PM"],
        "Dr. Mariam Hassan ": ["06:00 PM", "07:00 PM"],
    }
    
class patient(Doctors):
    def __init__(self):
        self.doctor_list = copy.deepcopy(Doctors.doctor_list) 
        self.available_times = copy.deepcopy(Doctors.available_times)
        self.name = ""
        self.age = 0
        self.phone = "" 
        self.gender = ""
        self.appointment = None
        
    all_appointments = []
    def bookAppointment(self):
        print ("\n   Enter patient info   ")
        
        # 1. إدخال الاسم
        self.name = input("Enter patient name : ").strip()
        
        # 2. إدخال الجنس والتحقق منه
        while True:
            self.gender = input("Enter Gender (Male/Female): ").strip().lower()
            if self.gender in ["male", "female"]:
                break
            print(" Invalid input. Please enter 'Male' or 'Female'.")
        
        # 3. إدخال العمر والتحقق منه
        while True:
            try:
                age_input = input("Enter Age: ").strip()
                self.age = int(age_input)
                if self.age > 0:
                    break
                print(" Age must be a positive number.")
            except ValueError:
                print(" Invalid input. Please enter a valid number for age.")
        
        # 4. إدخال رقم الهاتف 
        self.phone = input("Enter Phone Number: ").strip()
        
        print(f"\n Patient {self.name} info recorded. Starting appointment selection...")

        # 5. الانتقال لاختيار التخصص والطبيب (is_booking=True لتفعيل منطق الاختيار)
        self.choose_specialty(is_booking=True) 

    
    def choose_specialty(self, is_booking=False): 
        
        print("\n Available Specialities : ")
        specialties = sorted(self.doctor_list.keys()) 
        
        for i, specialty in enumerate(specialties):
            print(f"{i + 1}- {specialty}")
            
        while True:
            try:
                choice = int(input(f"Choose specialty by number (1 to {len(specialties)}): ").strip())
                if 1 <= choice <= len(specialties):
                    selected_specialty = specialties[choice - 1]
                    break
                print(f" Invalid number. Please enter a number between 1 and {len(specialties)}.")
            except ValueError:
                print(" Invalid input. Please enter a valid number.")
                
        print(f"\n You selected: {selected_specialty}")
        
        # عرض الأطباء المتاحين في التخصص المختار
        available_doctors = self.doctor_list.get(selected_specialty, [])
        doctors_with_slots = {}
        
        print(f" Available Doctors in {selected_specialty} ")
        
        doc_counter = 1
        for doc_name in available_doctors:
            
        
            # تنظيف الاسم مرة واحدة قبل البحث والعرض
            clean_name = doc_name
            slots = self.available_times.get(doc_name, [])
            
            
            if slots:
                doctors_with_slots[str(doc_counter)] = {'name': clean_name, 'slots': slots}
                slots_str = ", ".join(slots)
                print(f"{doc_counter}- {clean_name} | Slots: {slots_str}")
                doc_counter += 1

        if not doctors_with_slots:
            print(" No doctors with available times found at the moment.")
            return

        if not is_booking:
            print("\n  Note : To book, choose option '1' from the main menu.")
            return
        
        # منطق اختيار الطبيب والموعد إذا كان حجزاً
        while True:
            doc_choice = input(f"Enter the number of the desired doctor (1 to {len(doctors_with_slots)}): ").strip()
            if doc_choice in doctors_with_slots:
                selected_doctor_info = doctors_with_slots[doc_choice]
                selected_doctor_name = selected_doctor_info['name']
                available_slots = selected_doctor_info['slots']
                break
            print(f" Invalid input. Please enter a number between 1 and {len(doctors_with_slots)}.")
        
        print(f"\n You selected: {selected_doctor_name}")
        
        # اختيار الموعد
        print("\n  Available appointments  ")
        slot_map = {}
        for i, slot in enumerate(available_slots):
            slot_map[str(i + 1)] = slot
            print(f"{i + 1}- {slot}")

        while True:
            
            
            slot_choice = input(f"Enter the number of the desired slot (1 to {len(available_slots)}): ").strip()
            if slot_choice in slot_map:
                selected_time = slot_map[slot_choice]

        # التحقق إن المعاد لسه متاح
            if selected_time not in self.available_times[selected_doctor_name]:
                print("\n This appointment is already booked. Please choose another one.")
                return  # يرجع علشان يبدأ الحجز من جديد

        # تسجيل الموعد
            self.appointment = {
            'doctor': selected_doctor_name,
            'time': selected_time,
            'specialty': selected_specialty
        }

        # حذف المعاد من قائمة المتاح
            self.available_times[selected_doctor_name].remove(selected_time)
        
          # حفظ الحجز
            patient.all_appointments.append({
              
              "patient": self.name,
              "age": self.age,
              "gender": self.gender,
              "phone": self.phone,
              "doctor": selected_doctor_name,
              "specialty": selected_specialty,
              "time": selected_time
            })
            break

        print(f" Invalid input. Please enter a number between 1 and {len(available_slots)}.")
        

    
    def sendFeedback(self):
        
        display_name = self.name.title() if self.name else 'Patient'
        feedback = input(f"Dear {display_name}, please Enter your Feedback: ").strip()
        if feedback:
            print(f" Thank you, Your feedback has been received.")
            print(f"> Feedback: \"{feedback}\"")
        else:
            print("Received empty feedback.")

    def patientMenu(self):
        
        while True:
            print("\n==============================")
            print("  Patient Menu  ")
            print("1- Book Appointment (Enter Data & Choose Slot)")
            print("2- Choose Speciality (View Doctors Only)")
            print("3- Send Feedback")
            print("4- Exit ")
            print("==============================")
            
            chosse = input("Enter num from 1 to 4: ").strip()
            
            if chosse == '1':
                # عند اختيار 1، يتم استدعاء bookAppointment التي بدورها تستدعي choose_specialty(is_booking=True)
                self.bookAppointment()
            
            elif chosse == '2':
                # عند اختيار 2، يتم استدعاء choose_specialty(is_booking=False) لعرض التخصصات فقط
                self.choose_specialty(is_booking=False)
            elif chosse == '3':
                self.sendFeedback()
            elif chosse == '4':
                print(f" Exiting program.")
                return
            else:
                print("Invalid input. Please enter a number between 1 and 4.")


obj = patient() 
obj.patientMenu()