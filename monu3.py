import datetime

# Hospital Management System Class
class HospitalApp:
    def __init__(self):
        self.patients = {}  # Patient ID will be the key

    def add_patient(self):
        patient_id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        age = input("Enter Patient Age: ")
        disease = input("Enter Disease: ")
        admission_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Add patient to the dictionary
        self.patients[patient_id] = {
            "Name": name,
            "Age": age,
            "Disease": disease,
            "Admission Date": admission_date
        }
        print(f"Patient {name} added successfully!")

    def view_patient(self):
        patient_id = input("Enter Patient ID to view: ")
        if patient_id in self.patients:
            print(f"Patient ID: {patient_id}")
            for key, value in self.patients[patient_id].items():
                print(f"{key}: {value}")
        else:
            print("Patient not found.")

    def update_patient(self):
        patient_id = input("Enter Patient ID to update: ")
        if patient_id in self.patients:
            print("Choose what to update:")
            print("1. Name")
            print("2. Age")
            print("3. Disease")
            choice = input("Enter choice (1/2/3): ")
            
            if choice == '1':
                new_name = input("Enter new Name: ")
                self.patients[patient_id]["Name"] = new_name
            elif choice == '2':
                new_age = input("Enter new Age: ")
                self.patients[patient_id]["Age"] = new_age
            elif choice == '3':
                new_disease = input("Enter new Disease: ")
                self.patients[patient_id]["Disease"] = new_disease
            else:
                print("Invalid choice.")
            print("Patient information updated successfully!")
        else:
            print("Patient not found.")

    def delete_patient(self):
        patient_id = input("Enter Patient ID to delete: ")
        if patient_id in self.patients:
            del self.patients[patient_id]
            print(f"Patient ID {patient_id} deleted successfully!")
        else:
            print("Patient not found.")

    def list_patients(self):
        if not self.patients:
            print("No patients in the system.")
        else:
            print("List of all patients:")
            for patient_id, info in self.patients.items():
                print(f"ID: {patient_id} | Name: {info['Name']} | Disease: {info['Disease']}")

# Function to run the application
def main():
    app = HospitalApp()

    while True:
        print("\n--- Hospital Management System ---")
        print("1. Add Patient")
        print("2. View Patient")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. List All Patients")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            app.add_patient()
        elif choice == '2':
            app.view_patient()
        elif choice == '3':
            app.update_patient()
        elif choice == '4':
            app.delete_patient()
        elif choice == '5':
            app.list_patients()
        elif choice == '6':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
