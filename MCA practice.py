#Lists
"""names=["Dinesh","Sasi","Chinni"]
for i in names:
    print(i)"""

"""l=[34,34,2.4,False]
l[2]=3.5
print(l)
print(l[2])

for i in range(0,5):
    print(i)
list=[24,12,36,85,42]
list.append(99)
list.append(102)
list.insert(5,72)
list.remove(12)
list.pop(6)
print(len(list))"""



"""nums=[10,20,30,40]
print(30 in nums)
print(50 not in nums)"""

"""nums=[4,2,8,1,5]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)"""

"""numbers=[10,20,30,40,50,60]
num=[1,2]+[3,4]
num2=[1,2]*2
num3=3 in [1,2,3]
print(numbers[10:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[::-1])
print(num)
print(num2)
print(num3)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))"""

"""numbers=[25,12,18,45,60]
item=int(input("Enter a number:"))
if item in numbers:
    print("found")
else:
    print("not found")"""

"""n=int(input("How many numbers to be stored in list:"))
numlist=[]
evenlist=[]
oddlist=[]
for i in range(n):
    numbers=int(input("enter a number:"))
    numlist.append(numbers)
for i in numlist:
    if i>0:
        if i%2==0:
            evenlist.append(i)
        else:
            oddlist.append(i)
print("The number list")
for i in numlist:
    print(i)
print("The even list")
if i in evenlist:
    print(i)
print("The odd list")
if i in oddlist:
    print(i)"""

"""print("Hello world")
x=10
y=20
print("X=",x,"Y=",y)
print(1,2,3,sep=",")
print("Hello",end=" ")
print("World")"""

"""name="DINESH KUMAR"
print("MY NAME IS",name)"""

"""a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
print("integer division:",a//b)
print("Float division:",a/b)
print("Remainder:",a%b)"""

"""n=int(input("Enter no of rows:"))
for i in range(1,n+1):
    print("*"*i)"""

"""for i in range(4):
    print("123")"""

"""d1={101:"rahul",102:21,103:"MTech"}
print(d1)
d1.pop(102)
print(d1)
d1.popitem()
print(d1)
del d1[101]
print(d1)
d1.clear
print(d1)"""

"""students={
#    "s1":{"name":"Aman","age":21,"course":"Mtech"},
    "s2":{"name":"Priya","age":22,"Course":"MCA"}
}
students.update({"city":"Bhopal"})
print(students)
#print(students["s1"]["name"])"""
"""print(len(student))
print("name"in student)
print(student.keys())
print(student.values())
print(student.items())"""
"""for key in student:
    print(key,":",student[key])"""

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


