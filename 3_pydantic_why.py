from pydantic import BaseModel
from typing import List,Dict

class Patient(BaseModel):

    name:str
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Inserted")


patient_info = {'name':'Satyam','age':'20','weight':'75','married':'False','allergies':['None'],'contact_details':{'phone':'309248','email':'cjsbfjb'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
