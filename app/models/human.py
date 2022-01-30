from app import db
class Human(db.Model):
    username=db.Column(db.String, primary_key=True)
    zipcode=db.Column(db.Integer)
    pets = db.relationship("Pet", backref="human", lazy=True)

    def convert_human_to_dict(self):
        return {"username": self.username,
                "zipcode": self.zipcode}