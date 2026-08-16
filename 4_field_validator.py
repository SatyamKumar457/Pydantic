from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        #abc@gmail.com

        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a Valid domain.")

        return value

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')


patient_info = {'name':'Satyam Kumar','email':'satyam@icici.com','age':'20','weight':75, 'married': False, 'allergies':['pollen', 'dust'], 'contact_details':{'phone':'4234213'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)