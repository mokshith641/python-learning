from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, pid, name, age):
        self._pid = pid
        self._name = name
        self._age = age

    def get_id(self):
        return self._pid

    def get_name(self):
        return self._name

    @abstractmethod
    def display(self):
        pass


class Doctor(Person):
    def __init__(self, did, name, age, specialization):
        super().__init__(did, name, age)
        self._specialization = specialization

    def get_specialization(self):
        return self._specialization

    def display(self):
        print(f"Doctor ID: {self._pid}")
        print(f"Name: Dr. {self._name}")
        print(f"Age: {self._age}")
        print(f"Specialization: {self._specialization}")


class Patient(Person):
    def __init__(self, pid, name, age, disease):
        super().__init__(pid, name, age)
        self._disease = disease
        self._doctor = None

    def assign_doctor(self, doctor):
        self._doctor = doctor

    def display(self):
        print(f"\nPatient ID: {self._pid}")
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Disease: {self._disease}")

        if self._doctor:
            print(f"Doctor: Dr. {self._doctor.get_name()} ({self._doctor.get_specialization()})")
        else:
            print("Doctor: Not assigned")


class Hospital:
    def __init__(self):
        self._patients = {}
        self._doctors = {}

    def add_doctor(self):
        did = input("Enter Doctor ID: ")

        if did in self._doctors:
            print("Doctor ID already exists")
            return

        name = input("Enter Doctor Name: ")
        age = int(input("Enter Age: "))
        specialization = input("Enter Specialization: ")

        doctor = Doctor(did, name, age, specialization)
        self._doctors[did] = doctor
        print("Doctor added successfully")

    def add_patient(self):
        pid = input("Enter Patient ID: ")

        if pid in self._patients:
            print("Patient ID already exists")
            return

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        disease = input("Enter Disease: ")

        patient = Patient(pid, name, age, disease)
        self._patients[pid] = patient
        print("Patient added successfully")

    def assign_doctor(self):
        pid = input("Enter Patient ID: ")

        if pid not in self._patients:
            print("Patient not found")
            return

        if not self._doctors:
            print("No doctors available")
            return

        patient = self._patients[pid]

        print("\nAvailable Doctors:")
        doctor_list = list(self._doctors.values())

        for i, d in enumerate(doctor_list):
            print(f"{i + 1}. Dr. {d.get_name()} - {d.get_specialization()}")

        choice = int(input("Select doctor number: ")) - 1

        if 0 <= choice < len(doctor_list):
            patient.assign_doctor(doctor_list[choice])
            print("Doctor assigned successfully")
        else:
            print("Invalid choice")

    def show_all(self):
        if not self._patients and not self._doctors:
            print("No data available")
            return

        print("\n--- Doctors ---")
        for d in self._doctors.values():
            d.display()
            print()

        print("\n--- Patients ---")
        for p in self._patients.values():
            p.display()


hospital = Hospital()

while True:
    print("\n===== Hospital Menu =====")
    print("1. Add Doctor")
    print("2. Add Patient")
    print("3. Assign Doctor to Patient")
    print("4. Show All Data")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        hospital.add_doctor()
    elif choice == "2":
        hospital.add_patient()
    elif choice == "3":
        hospital.assign_doctor()
    elif choice == "4":
        hospital.show_all()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice")