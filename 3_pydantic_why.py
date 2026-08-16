from pydantic import BaseModel,EmailStr,AnyUrl
from typing import List,Dict,Optional

class Patient(BaseModel):

    name:str
    email:EmailStr
    linkedin_url:AnyUrl
    age:int
    weight:float
    married:bool = False
    allergies:Optional[List[str]]=None
    contact_details:Dict[str,str]

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.linkedin_url)
    print("Inserted")


patient_info = {'name':'Satyam','email':'satyam@gmail.com','age':'20','weight':'75','married':'False','allergies':['None'],'contact_details':{'phone':'309248','email':'cjsbfjb'},'linkedin_url':'http://satyam.com'}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
