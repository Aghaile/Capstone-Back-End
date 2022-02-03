from app import db
import uuid
class Pet(db.Model):
    pet_id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    #another attribute cause psql doesn't share uuid generator 
    login=db.Column(db.String, default=uuid.uuid4().hex[:5],nullable=False)
    name=db.Column(db.String, nullable=False)
    bio=db.Column(db.String, nullable=True)
    age=db.Column(db.Integer, autoincrement=True)
    gender=db.Column(db.String, nullable=True)
    species=db.Column(db.String, nullable=True)
    zipcode=db.Column(db.Integer, nullable=False)
    phone_number=db.Column(db.String(10), nullable = False)
    

    def convert_pet_to_dict(self):
        return {"pet_id": self.pet_id,
                "name": self.name,
                "bio": self.bio,
                "age":self.age, 
                "gender": self.gender,
                "species": self.species,
                "zipcode": self.zipcode,
                "phone_number": self.phone_number,
                "login": self.login,}