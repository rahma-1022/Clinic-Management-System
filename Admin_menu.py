from Patient import patient
from Emergency_class import Emergency
class AdminSystem(patient, Emergency):
    def __init__(self):
        super().__init__()
        self.specialties = {
            "SP01":"Ophthalmology",
            "SP02":"Cardiovascular",
            "SP03":"Pediatrics",
            "SP04":"Neonatology",
            "SP05":"Dermatology",
            "SP06":"Orthopedics",
            "SP07":"Otolaryngology",
            "SP08":"Internal Medicine and Gastroenterology",
            "SP09":"Obstetrics and Gynecology",
            "SP10":"Physical therapy",
            "SP11":"Dentistry",
            "SP12":"Nutrition"
        }
        
        self.doctors_list = [   
            {
                "id":10101,  "name": "Mohamed Hassan", "specialty name": self.specialties["SP01"], "work hours": "08:00 AM - 03:00 PM"
            },
            {
                "id":10102, "name": "Sara Mahmoud", "specialty name": self.specialties["SP01"], "work hours": "08:00 AM - 03:00 PM"  
            },
            {
                "id":10103, "name": "Emily Clark", "specialty name": self.specialties["SP01"], "work hours": "03:00 PM - 10:00 PM" 
            },
            {
                "id":10104, "name": "Karim Abdullah", "specialty name": self.specialties["SP01"], "work hours": "03:00 PM - 10:00 PM"
            },
            {
                "id":10201, "name": "Adam Gamal", "specialty name": self.specialties["SP02"], "work hours": "08:00 AM - 03:00 PM"
            },
            {
                "id":10202, "name": "Layla Mustafa", "specialty name": self.specialties["SP02"], "work hours": "08:00 AM - 03:00 PM"
            },
            {
                "id":10203, "name": "Mark Williams", "specialty name": self.specialties["SP02"], "work hours": "03:00 PM - 10:00 PM"
            },
            {
                "id":10204, "name": "Yasmin Rami", "specialty name": self.specialties["SP02"], "work hours": "03:00 PM - 10:00 PM"
            },
            {
                "id":10301, "name": "Elizabeth Taylor", "specialty name": self.specialties["SP03"], "work hours": "08:00 AM - 03:00 PM"
            },
            {
                "id":10302, "name": "Khaled Walid", "specialty name": self.specialties["SP03"], "work hours": "08:00 AM - 03:00 PM"
            },
            {
                "id":10303, "name": "Fares Ahmed", "specialty name": self.specialties["SP03"], "work hours": "03:00 PM - 10:00 PM"
            },
            {
                "id":10304, "name": "Nada Karim", "specialty name": self.specialties["SP03"],"work hours": "03:00 PM - 10:00 PM"
            },
            {
                "id":10401, "name": "Lena Johnson", "specialty name": self.specialties["SP04"], "work hours": "08:00 AM - 03:00 PM"
            },
            {
                "id":10402, "name": "Peter Schmidt", "specialty name": self.specialties["SP04"], "work hours": "08:00 AM - 03:00 PM"
            },
            {
                "id":10403, "name": "Jana Ahmed", "specialty name": self.specialties["SP04"], "work hours": "03:00 PM - 10:00 PM"
            },
            {
                "id":10404, "name": "Mahmoud Tarek", "specialty name": self.specialties["SP04"], "work hours": "03:00 PM - 10:00 PM"
            },
            {
                "id":10501, "name": "Basel Mahmoud", "specialty name": self.specialties["SP05"], "work hours": "08:00 AM - 03:00 PM"
            },
            {
                "id":10502, "name": "Dalia Rushdi", "specialty name": self.specialties["SP05"], "work hours": "08:00 AM - 03:00 PM"
            },
            {
                "id":10503, "name": "Sophia Patel", "specialty name": self.specialties["SP05"], "work hours": "03:00 PM - 10:00 PM"
            },
            {
                "id":10504, "name": "Ali Mohamed", "specialty name": self.specialties["SP05"], "work hours": "03:00 PM - 10:00 PM"
            },
            {
                "id":10601, "name": "Hassan Gamal", "specialty name": self.specialties["SP06"], "work hours": "08:00 AM - 03:00 PM"
            },
            {
                "id":10602, "name": "Salma Hany", "specialty name": self.specialties["SP06"], "work hours": "08:00 AM - 03:00 PM"
            },
            {
                "id":10603, "name": "Maria Garcia", "specialty name": self.specialties["SP06"], "work hours": "03:00 PM - 10:00 PM"
            },
            {
                "id":10604, "name": "Ali samir", "specialty name": self.specialties["SP06"], "work hours": "03:00 PM - 10:00 PM"
            },
            {
                "id":10701, "name": "Mohamed Yasser", "specialty name": self.specialties["SP07"], "work hours": "08:00 AM - 03:00 PM"
            },
            {
                "id":10702, "name": "Ayat Nasser", "specialty name": self.specialties["SP07"], "work hours": "08:00 AM - 03:00 PM"
            },
            {
                "id":10703, "name": "Lena Taylor", "specialty name": self.specialties["SP07"], "work hours": "03:00 PM - 10:00 PM"
            },
            {
                "id":10704, "name": "Mohamed Hassan", "specialty name": self.specialties["SP07"], "work hours": "03:00 PM - 10:00 PM"
            },
            {
                "id":10801, "name": "Hossam Ali ", "specialty name": self.specialties["SP08"], "work hours": "08:00 AM - 03:00 PM"
            },
            {
                "id":10802, "name": "Omnia Ahmed", "specialty name": self.specialties["SP08"], "work hours": "08:00 AM - 03:00 PM"
            },
            {
                "id":10803, "name": "Reem Osama", "specialty name": self.specialties["SP08"], "work hours": "03:00 PM - 10:00 PM"
            },
            {
                "id":10804, "name": "Rajeev Mehra", "specialty name": self.specialties["SP08"], "work hours": "03:00 PM - 10:00 PM"
            },
            {
                "id":10901, "name": "Alia saeed", "specialty name": self.specialties["SP09"], "work hours": "08:00 AM - 03:00 PM"
            },
            {
                "id":10902, "name": "Kong Lu", "specialty name": self.specialties["SP09"], "work hours": "08:00 AM - 03:00 PM"
            },
            {
                "id":10903, "name": "Ghada Nabil", "specialty name": self.specialties["SP09"], "work hours": "03:00 PM - 10:00 PM"
            },
            {
                "id":10904, "name": "Fares Mahmoud", "specialty name": self.specialties["SP09"], "work hours": "03:00 PM - 10:00 PM"
            },
            {
                "id":11001, "name": "Lin Chen", "specialty name": self.specialties["SP10"], "work hours": "08:00 AM - 03:00 PM"
            },
            {
                "id":11002, "name": "Abdullah Mohamed", "specialty name": self.specialties["SP10"], "work hours": "08:00 AM - 03:00 PM"
            },
            {
                "id":11003, "name": "Seif Ahmed", "specialty name": self.specialties["SP10"], "work hours": "03:00 PM - 10:00 PM"
            },
            {
                "id":11004, "name": "Mai Nguyen", "specialty name": self.specialties["SP10"], "work hours": "03:00 PM - 10:00 PM"
            },
            {
                "id":11101, "name": "Fahad Mohamed", "specialty name": self.specialties["SP11"], "work hours": "08:00 AM - 03:00 PM"
            },
            {
                "id":11102, "name": "Anita Clark", "specialty name": self.specialties["SP11"], "work hours": "08:00 AM - 03:00 PM"
            },
            {
                "id":11103, "name": "Basel Waleed", "specialty name": self.specialties["SP11"], "work hours": "03:00 PM - 10:00 PM"   
            },
            {
                "id":11104, "name": "Hoda Tarek", "specialty name": self.specialties["SP11"], "work hours": "03:00 PM - 10:00 PM"
            },
            {
                "id":11201, "name": "Moumen Hassan", "specialty name": self.specialties["SP12"], "work hours": "08:00 AM - 03:00 PM"
            },
            {
                "id":11202, "name": "Aya Tamer", "specialty name": self.specialties["SP12"], "work hours": "08:00 AM - 03:00 PM"
            },
            {
                "id":11203, "name": "Hana Mahmoud", "specialty name": self.specialties["SP12"], "work hours": "03:00 PM - 10:00 PM"
            },
            {
                "id":11204, "name": "Philippe Martin", "specialty name": self.specialties["SP12"], "work hours": "03:00 PM - 10:00 PM"
            }
        ]
        
        self.admins = [
            {"id":1, "Name":"Rahma", "Contact number":"01012345678"},
            {"id":2, "Name":"Ola", "Contact number":"01023456789"},
            {"id":3, "Name":"Alaa", "Contact number":"01034567891"},
            {"id":4, "Name":"Habiba", "Contact number":"01045678912"},
            {"id":5, "Name":"Mariam", "Contact number":"01056789123"},
            {"id":6, "Name":"Mohamed","Contact number":"01067891234"},
            {"id":7, "Name":"Omar", "Contact number":"01078912345"},
            {"id":8, "Name":"Hamed", "Contact number":"01089123456"}, 
            {"id":9, "Name":"Youssef","Contact number":"01091234567"},
            {"id":10, "Name":"Adel", "Contact number":"01098765432"}
            ]
        
    def adminMenu(self):
        print("*"*100)
        print("  Admin menu  ")
        while True:
            check=input("Enter the password ").strip()
            if check != '123456':
                print ("The password is wrong. please try agian")
            else:
                break
        while True:
           
            print("*"*100)
            print("Choose number from 1 to 10: ")
            print("1-View information about doctors")
            print("2-View appointments")
            print("3-View emergency cases")
            print("4-Add new doctor")
            print("5-Delete a doctor")
            print("6-Change doctor data")
            print("7-View information about admins")
            print("8-Delete an admin")
            print("9-Change admin data")
            print("10-Back to the main menu")
            choose=input().strip()
            match choose:
                case '1':
                    self.showDoctors()
                case '2':
                    self.showAppointments()
                case '3':
                    self.showEmergencyCases()
                case '4':
                    self.addDctor()
                case '5':
                    self.removeDoctor()
                case '6':
                    self.editDoctorData()
                case '7':
                    self.showAdmins()
                case '8':
                    self.deleteAdmin()
                case '9':
                    self.editAdminData()
                case '10':
                    break 
                case _ :
                    print ("Please enter a number from 1 to 10 ")
                    
    def showAdmins(self):
        print("-"*100)
        if not self.admins:
            return print("There is no admins")
        header = ["ID", "Name", "Contact number"]
        print(f"{header[0]:<5}  {header[1]:<10}  {header[2]:<18}")
        print("-"*40)
        for admin in self.admins :
            print(f"{admin["id"]:<5}  {admin["Name"]:<10}  {admin["Contact number"]:<18}")
            print("-"*40) 
            
    def showDoctors(self):
        header = ["ID", "Name", "Specialization", "Work hours"]
        print("-"*150)
        if not self.doctors_list:
            return print("There is no doctors")
        print(f"{header[0]:<10}    {header[1]:<20}    {header[2]:<50}    {header[3]:<30}")
        print("-"*150)
        for doctor in self.doctors_list :
            print(f"{doctor["id"]:<10}    {doctor["name"]:<20}    {doctor["specialty name"]:<50}    {doctor["work hours"]:<30} ")
            print("-"*150)
            
    def showAppointments(self):
        header = ["patient", "age","gender", "phone", "doctor", "specialty", "time" ]
        print("-"*150)
        
        if not self.all_appointments:
            print("\n No appointments found.")
            print("-"*150) 
            return
        
        print(f"{header[0]:<20}  {header[1]:<8}  {header[2]:<10}  {header[3]:<15}  {header[4]:<20}  {header[5]:<30}  {header[6]:<20}")
        print("-"*150)
        for p in self.all_appointments: 
            print(f"{p['patient']:<20}  {p['age']:<8}  {p['gender']:<10}  {p['phone']:<15}  {p['doctor']:<20}  {p['specialty']:<30}  {p['time']:<20}")
            print("-"*150)
        print("-"*150)     
        
    def addDctor(self):
        new_doctor_name = input("Enter the name of the doctor: ")
        new_doctor_specialty = input("Enter the specialty of the doctor: ")
        new_doctor_work_hours = input("Enter the work hours of the doctor: ")
        while True:
            try:
                new_doctor_id = int(input("Enter the id of the doctor: ").strip())
                break
            except ValueError:
                print("The id must be an integer. Please try again")
        for doctor in self.doctors_list:
            if new_doctor_id == doctor["id"] :
                return print("Doctor already exists")
        Doctor ={
            "name" : new_doctor_name,
            "specialty name":new_doctor_specialty,
            "id":new_doctor_id,
            "work hours":new_doctor_work_hours 
        } 
        self.doctors_list.append(Doctor) 
        return print("Doctor added successfully")
    
    def showEmergencyCases(self):
        header1 = ["Address", "Description", "Contact number"]
        header2 = ["Address","Case type", "Contact number"]
        print("-"*150)
        if self.send_ambulance :
            print("   The emergency cases  ")
            print(f"{header1[0]:<40}  {header1[1]:<60}  {header1[2]:<15}")
            print("-"*150)
            for e in self.send_ambulance :
                print(f"{e['patient address']:<40}  {e['description']:<60}  {e['contact number']:<15}")
                print("-"*150)
                break
        else :
            print ("There is no emergency casses")
            print("-"*150)
               
        if self.send_nurse:
            print("   Patients who requested nurses   ")
            print(f"{header2[0]:<40}  {header2[1]:<60}  {header2[2]:<15}")
            print("-"*150)
            for e in self.send_nurse :
                print(f"{e['address']:<40}  {e['case type']:<60}  {e['contact number']:<15}")
                print("-"*150)
                break 
        else :    
            print ("There is no patients have requested nurses yet.")
            print("-"*150)
        print("-"*150)    
       
    def removeDoctor(self):
        doctor_found = False
        while True:
            try:
                id_of_doctor = int(input("Enter the id of the doctor you want to delete ").strip())
                break
            except ValueError:
                print("The id must be an integer. Please try again")
        for doctor_data in self.doctors_list:
            if  doctor_data['id'] == id_of_doctor:
                doctor_found = True
                check = input(f"Are you sure about deleting the data about Dr.{doctor_data['name']}?").strip().lower()
                if check == 'yes':
                    self.doctors_list.remove(doctor_data)
                    print("The doctor is successfully deleted.")
                    break
                elif check != 'yes':
                    break
        if doctor_found == False:
            print("There is no doctor that has this id.")
        
    def editDoctorData(self):
        doctor_found = False
        while True:
            try:
                id_of_doctor = int(input("Enter the id of the doctor you want to editing ").strip())
                break
            except ValueError:
                print("The id must be an integer. Please try again")
        for doctor_data in self.doctors_list:
            if  doctor_data['id'] == id_of_doctor:
                doctor_found= True
                check = input(f"Are you sure about editing data about Dr.{doctor_data['name']}?").strip().lower()
                if check == 'yes':
                    ask = input("Which data that you want to change?\n1-ID.\n2-Specialization.\n3-Work hours.\n").strip()
                    match ask :
                        case '1':
                            while True:
                                try:
                                    change = int(input("Enter the new id ").strip())
                                    break
                                except ValueError:
                                    print("The id must be an integer. Please try again")  
                            doctor_data['id'] = change
                            print(f"The id of Dr.{doctor_data['name']} is successfully editing")
                            break
                        case '2':
                            change = input("Enter the new specialty ").strip()
                            doctor_data['specialty name'] = change
                            print(f"The specialization of Dr.{doctor_data['name']} is successfully editing")
                            break
                        case '3':
                            change = input("Enter the new id ").strip()
                            doctor_data['work hours'] = change
                            print(f"The work hours of Dr.{doctor_data['name']} is successfully editing")
                            break
                elif check != 'yes':
                    break
        if doctor_found == False:
            print("There is no doctor that has this id.")
        
    def deleteAdmin(self):
        admin_found = False
        while True:
            try:
                id_of_admin = int(input("Enter the id of the admin you want to delete ").strip())
                break
            except ValueError:
                print("The id must be an integer. Please try again")
        for admin_data in self.admins:
            if  admin_data['id'] == id_of_admin:
                admin_found = True
                check = input(f"Are you sure about deleting the data about {admin_data['Name']}?").strip().lower()
                if check == 'yes':
                    self.admins.remove(admin_data)
                    print("The admin is successfully deleted.")
                    break
                elif check != 'yes':
                    break
        if admin_found == False:
            print("There is no admin that has this id.")
        
    def editAdminData(self):
        admin_found = False
        while True:
            try:
                id_of_admin = int(input("Enter the id of the admin you want to editing ").strip())
                break
            except ValueError:
                print("The id must be an integer. Please try again")
        for admin_data in self.admins:
            if  admin_data['id'] == id_of_admin:
                admin_found= True
                check = input(f"Are you sure about editing data about {admin_data['Name']}?").strip().lower()
                if check == 'yes':
                    ask = input("Which data that you want to change?\n1-ID.\n2-Contact number\n").strip()
                    match ask :
                        case '1':
                            while True:
                                try:
                                    change = int(input("Enter the new id ").strip())
                                    break
                                except ValueError:
                                    print("The id must be an integer. Please try again")
                            admin_data['id'] = change
                            print(f"The id of {admin_data['Name']} is successfully editing")
                            break
                        case '2':
                            change = input("Enter the new contact number ").strip()
                            admin_data['Contact number'] = change
                            print(f"The contact number of {admin_data['Name']} is successfully editing")
                            break
                elif check != 'yes':
                    break
        if admin_found == False:
            print("There is no admin that has this id.")  
        
d1=AdminSystem()
d1.adminMenu()