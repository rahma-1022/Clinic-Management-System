class Emergency:
    send_ambulance = []
    send_nurse = []
    def emergencyMenu(self):
        """
        View the ambulance list
        """
        print("The ambulance list:")
        print("1.Send an ambulance")
        print("2.Send a nurse")

    def sendAmbulance(self):
        """
        Send an ambulance to the location of the incident

        inputs:
        The adress:adress(str)
        Description of the condition:description(str)
        Contact number:contact_number (str)
        Outputs:
        Confirmattion of ambulance dispatch: str   """
        address =input("Enter the address:")
        description = input("Enter the description of the condition:")
        contact_number =input("Enter the contact number:")
        print(f"Send an ambulance to {address}...")
        print(f"Description of the condition:{description}")
        print(f"Contact number: {contact_number}")
        Emergency.send_ambulance.append(
            {
                "patient address":address, "description":description, "contact number":contact_number
            }
        )
        return "The ambulance was successfully dispatched."
    def sendNurse(self):
        """
        Send a nurse for an urgent case

        inputs:
        The address:address(str)
        The case type:case_type(str)
        The contact number:contact_number (str)
        Outputs:
        Confirmation of sending a nurse:str
        """
        address =input("Enter the address:")
        case_type =input("Enter the case type:")
        contact_number =input("Enter the contact number:")
        print(f"Send a nurse to {address}...")
        print(f"The case type:{case_type}")
        print(f"Contact number:{contact_number}")
        Emergency.send_nurse.append(
            {
                "address":address, "case type":case_type, "contact number":contact_number
            }
        )
        return "A nurse was successfully send"

if __name__ == "__main__":
    emergency = Emergency()
    emergency.emergencyMenu()
    choice = input("If you want an ambulance enter number(1), if you want a nurse enter number(2): ")
    if choice == "1":
        print(emergency.sendAmbulance())
    elif choice == "2":
        print(emergency.sendNurse())