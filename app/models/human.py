from app import db
class Human(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    username=db.Column(db.String)
    zipcode=db.Column(db.Int)

    def convert_human_to_dict(self):
        return { "id": self.id,
                "username": self.username,
                "zipcode": self.zipcode}