from app import db
class Pet(db.Model):
    name=db.Column(db.String, primary_key=True)
    bio=db.Column(db.String)
    age=db.Column(db.Integer)
    username=db.Column(db.String, db.ForeignKey('human.username'), nullable=False)
    zipcode=db.Column(db.Integer, db.ForeignKey('human.username'), nullable=False)
    # human=db.relationship('Human', backref='pet')


    def convert_pet_to_dict(self):
        return {"name": self.name,
                "zipcode": self.zipcode,
                "bio": self.bio,
                "age":self.age}