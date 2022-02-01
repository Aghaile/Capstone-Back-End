from app import db
class Pet(db.Model):
    pet_id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    bio=db.Column(db.String)
    age=db.Column(db.Integer, autoincrement=True)
    gender=db.Column(db.String)
    species=db.Column(db.String)
    zipcode=db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.Integer, nullable = False)
    

    def convert_pet_to_dict(self):
        return {"name": self.name,
                "bio": self.bio,
                "age":self.age, 
                "gender": self.gender,
                "species": self.species,
                "zipcode": self.zipcode,
                "phone_number": self.phone_number}