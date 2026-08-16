from pydantic import BaseModel,EmailStr,AnyUrl, Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title="Name of the Patient", description="Give the name of the patient in less than 50 chars", examples=['Satyam','Amit'])]
    email:EmailStr
    linkedin_url:AnyUrl
    age:int = Field(gt=0,lt=120)
    weight:Annotated[float , Field(gt=0,strict=True)]
    married: Annotated[bool, Field(default=None, description="Is the patient married or not.")]
    allergies:Annotated[Optional[List[str]],Field(default=None,max_length=5)]
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


patient_info = {'name':'Satyam','email':'satyam@gmail.com','age':'20','weight':75,'married':'False','allergies':['None'],'contact_details':{'phone':'309248','email':'cjsbfjb'},'linkedin_url':'http://satyam.com'}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
