from app import db
class Pet(db.Model):
    pet_id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String,)
    bio=db.Column(db.String)
    age=db.Column(db.Integer)
    gender=db.Column(db.String)
    species=db.Column(db.String)
    zipcode=db.Column(db.Integer, nullable=False)
    
    


    # def convert_pet_to_dict(self):
    #     return {"name": self.name,
    #             "zipcode": self.zipcode,
    #             "bio": self.bio,
    #             "age":self.age}