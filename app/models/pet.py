from app import db
class Pet(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String)
    zipcode=db.Column(db.Int)

    def convert_pet_to_dict(self):
        return { "id": self.id,
                "name": self.name,
                "zipcode": self.zipcode}