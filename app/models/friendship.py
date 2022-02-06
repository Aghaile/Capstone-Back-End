from app import db
class Friendship(db.Model):
    friendship_id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    pet=db.relationship("Pet", backref="friendships")
    pet_id=db.Column(db.Integer, db.ForeignKey("pet.id"), nullable=False)
    pals=db.Column(db.Boolean, default=False)