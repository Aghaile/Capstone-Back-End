from app import db
import uuid 

class Pet(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement = True)
    name=db.Column(db.String, nullable=False)
    bio=db.Column(db.String) 
    age=db.Column(db.Integer)
    gender=db.Column(db.String)
    species=db.Column(db.String)
    zipcode=db.Column(db.Integer, nullable=False)
    phone=db.Column(db.String(10), nullable = False)
    #pull phone number library into front and back end 
    #e164
    

    def convert_pet_to_dict(self):
        return {"id": self.id,
                "name": self.name,
                "bio": self.bio,
                "age":self.age, 
                "gender": self.gender,
                "species": self.species,
                "zipcode": self.zipcode,
                "phone": self.phone}