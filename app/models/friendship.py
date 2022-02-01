from app import db
class Friendship(db.Model):
    friendship_id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    pal=db.relationship("pet", backref="pal")
    pal_id=db.Column(db.Integer, db.ForeignKey("pal.id"), nullable=False)
    potential_pals=db.Column(db.Boolean, default=False)
    pending_pals=db.Column(db.Boolean, default=False)
    pawsitively_pals=db.Column(db.Boolean, default=False)