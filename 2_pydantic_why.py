from pydantic import BaseModel

class Patient(BaseModel):

    name: str
    age: int

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print("Inserted")


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print("Updated")

patient_info = {'name':'Satyam','age':20}

patient1 = Patient(**patient_info) # ** Means Unpacking

insert_patient_data(patient1)

update_patient_data(patient1)