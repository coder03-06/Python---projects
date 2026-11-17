
print("---------- Hospital Management System ----------")
print("-------------------------------------------------")

doctors = [
    {"id": "DR001", "name": "Dr. Meera Nair", "spec": "General Surgeon", "fee": 500},
    {"id": "DR002", "name": "Dr. Arjun Rao", "spec": "Cardiology", "fee": 800},
    {"id": "DR003", "name": "Dr. Sana Ali", "spec": "General Medicine", "fee": 400},
]

patients = []
appointments = []


class Person:
    def __init__(self, name, phone, age, gender, date):
        self.name = name
        self.phone = phone
        self.age = age
        self.gender = gender
        self.date = date

class Patient(Person):
    def __init__(self, name, phone, age, gender, date):
        super().__init__(name, phone, age, gender, date)

    def display(self):
        print(f"Name:   {self.name}")
        print(f"Age:    {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Phone:  {self.phone}")


while True:

    print("\n---------- Main Menu ----------")
    print("1. Admin Mode")
    print("2. User Mode")
    print("3. Exit")

    option = int(input("Enter your choice: "))

    if option == 1:

        while True:
            print("\n---------- Admin Mode ----------")
            print("1. View Appointments")
            print("2. View Doctors")
            print("3. Exit to Main Menu")

            choice = int(input("Enter your choice: "))

            if choice == 1:

                if not appointments:
                    print("No appointments found.")

                else:
                    print("\n---------- Appointments ----------")

                    for appointment in appointments:
                        print(f"Patient: {appointment['patient_name']}")
                        print(f"Age: {appointment['age']}")
                        print(f"Doctor: {appointment['doctor_name']}")
                        print(f"Date: {appointment['date']}")
                        print("----------------------------------")

            elif choice == 2:

                print("\n---------- Doctor Details ----------")

                for doctor in doctors:
                    print(f"ID: {doctor['id']}")
                    print(f"Name: {doctor['name']}")
                    print(f"Specialization: {doctor['spec']}")
                    print(f"Fee: Rs.{doctor['fee']}")
                    print("----------------------------------")

            elif choice == 3:
                print("Exiting Admin Mode...")
                break

            else:
                print("Invalid choice. Please try again.")


    elif option == 2:

        while True:
            print("\n---------- User Mode ----------")
            print("1. Book Appointment")
            print("2. Cancel Appointment")
            print("3. View Doctors")
            print("4. Exit to Main Menu")

            choice = int(input("Enter your choice: "))

            if choice == 1:

                patient_name = input("Enter your name: ")
                age = int(input("Enter your age: "))
                date = input("Enter appointment date (YYYY-MM-DD): ")
                phone = input("Enter your phone number: ")
                gender = input("Enter your gender: ")

                patient = Patient(patient_name, phone, age, gender, date)
                patients.append(patient)

                print("\nAvailable Doctors:")

                for doctor in doctors:
                    print(f"ID: {doctor['id']}, Name: {doctor['name']}, "
                          f"Specialization: {doctor['spec']}, Fee: Rs.{doctor['fee']}")

                doctor_id = input("\nEnter Doctor ID: ")

                selected_doctor = next(
                    (doctor for doctor in doctors if doctor["id"] == doctor_id),
                    None
                )

                if selected_doctor:

                    appointment = {
                        "patient_name": patient.name,
                        "age": patient.age,
                        "doctor_name": selected_doctor["name"],
                        "date": patient.date
                    }

                    appointments.append(appointment)

                    print("\nAppointment booked successfully!")
                    print(f"Doctor: {selected_doctor['name']}")
                    print(f"Date: {date}")
                    print(f"Fee: Rs.{selected_doctor['fee']}")

                else:
                    print("Invalid Doctor ID.")

            elif choice == 2:

                patient_name = input("Enter patient name: ")

                for appointment in appointments:

                    if appointment["patient_name"].lower() == patient_name.lower():

                        appointments.remove(appointment)
                        print("Appointment cancelled successfully!")
                        break

                else:
                    print("No appointment found for this patient.")


            elif choice == 3:

                print("\n---------- Available Doctors ----------")

                for doctor in doctors:
                    print(f"ID: {doctor['id']}, Name: {doctor['name']}, "
                          f"Specialization: {doctor['spec']}, Fee: Rs.{doctor['fee']}")

            elif choice == 4:
                print("Exiting User Mode...")
                break

            else:
                print("Invalid choice. Please try again.")


    elif option == 3:
        print("\nThank you for using Hospital Management System!")
        break

    else:
        print("Invalid option. Please try again.")
