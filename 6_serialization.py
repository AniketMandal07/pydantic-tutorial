from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    
    name: str
    gender: str
    age: int
    address: Address
    
address_dict = {'city': 'guwahati', 'state': 'assam', 'pin': '781007'}

address1 = Address(**address_dict)

patient_dict = {'name': 'aniket', 'gender': 'male', 'age': 19, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump_json(exclude_unset=True)

print(temp)
print(type(temp))
