from app import db
class Friendship(db.Model):
    friendship_id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    pet=db.relationship("Pet", backref="friendships")
    pal_id=db.Column(db.Integer, db.ForeignKey("pet.pet_id"), nullable=False)
    potential_pals=db.Column(db.Boolean, default=False)
    pending_pals=db.Column(db.Boolean, default=False)
    pawsitively_pals=db.Column(db.Boolean, default=False)