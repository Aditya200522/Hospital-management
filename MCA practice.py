#ASSIGNMENT
patients = {}

while True:
    print("\n====Hospital Patient Record System ====")
    print("1. Create Patient Record")
    print("2. Add Patient Record")
    print("3. View Patient Records")
    print("4. Update Patient Record")
    print("5. Delete Patient Record")
    print("6. Exit") # Corrected menu text


    choice = input("Enter your choice: ")

    
    if choice == "1":
        patient_id = input("Enter Patient ID: ")

        if patient_id in patients:
            print("Patient record already exists!")
        else:
            name = input("Enter Patient Name: ")
            age = int(input("Enter Patient Age: "))
            disease = input("Enter Patient Disease: ")

            patients[patient_id] = {
                "name" : name,
                "age"  : age,
                "disease": disease
            }

            print("Patient Record Created Successfully!")
    elif choice == "2":
        patient_id = input("Enter Patient Id: ")

        if patient_id in patients:
            print("Patient ID Already Exists")
        else:
            name = input("Enter Patient Name: ")
            age =  int(input("Enter Patient Age: "))
            disease = input("Enter Patient Disease: ")

            patients[patient_id] = {
                "name" : name,
                "age"  : age,
                "disease": disease
            }

            print("Patient Added Successfully!")
    elif choice == "3":
        if not patients:
            print("No Patient Records Found.")
        else:
            print("\nPatient Records:")
            for patient_id, details in patients.items():
                print("Patient ID:", patient_id)
                print("Name:", details["name"])
                print("Age:",details["age"])
                print("Disease:",details["disease"])
                print("-----------------------------")
    elif choice == "4":
        patient_id = input("Enter Patient ID To Update: ")

        if patient_id in patients:
            print("1. Update Name")
            print("2. Update Age")
            print("3. Update Disease")

            option = input("Choose Field To Update:")

           
            if option == "1":
                patients[patient_id]["name"] = input("Enter new name: ")
                print("Name updated successfully!")
            elif option == "2":
                # Fixed typo: changed patient_id to patients
                patients[patient_id]["age"] = int(input("Enter your new age: "))
                print("Age updated successfully!")
            elif option == "3":
                patients[patient_id]["disease"] = input("Enter new disease: ")
                print("Disease updated successfully!")
            else:
                print("Invalid update option!")
        else:
            print("Patient record not found!")
            
   
    elif choice == "5":
        patient_id = input("Enter Patient Id To Delete: ")   

        if patient_id in patients:
            del patients[patient_id]
            print("Patient record deleted successfully")
        else:
            print("Patient record not found!")
    elif choice == "6":
        print("Thank you for using the Hospital Patient Record System!")
        break
    else:
        print("Invalid choice. Please try again.")


