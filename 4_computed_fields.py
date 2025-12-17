from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    
    name: str 
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    
    
    
def update_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.contact_details)
    print(patient.allergies)
    print('BMI', patient.bmi)
    print('updated')

patient_info = {'name':'aniket', 'email': 'abc@hdfc.com', 'age': '19', 'weight': 52.4, 'height':1.68, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2853910876', 'emergency': '29272727'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)