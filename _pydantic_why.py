from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    
    name: Annotated [str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Aniket', 'Namit'])]
    email: EmailStr
    linkedIn_url: AnyUrl
    age: int
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default= None, max_lenght=5)]
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.contact_details)
    print(patient.allergies)
    print('inserted')
    
def update_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.contact_details)
    print(patient.allergies)
    print('updated')

patient_info = {'name':'aniket', 'email': 'abc@gmail.com', 'linkedIn_url':'http://linkedIn.com/0712', 'age': 19, 'weight': 52.4, 'contact_details':{'phone':'2853910876'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)