from app import db

class Pal(db.Model):
    friendship_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    adding_pal= db.Column(db.Integer, nullable=False)
    added_pal= db.Column(db.String, db.ForeignKey('pet.pal_id'), nullable=False)
    pet = db.relationship("Pet", backref="pals")
    user= db.relationship("User", backref="pals")


# class Friendship(db.Model):
#     friendship_id=db.Column(db.Integer, primary_key=True, autoincrement=True)
#     pet=db.relationship("Pet", backref="friendships")
#     requesting_pet=db.Column(db.Integer, db.ForeignKey("pet.id"), nullable=False)
#     requested_pal= db.Column(db.Integer, db.ForeignKey("pet.friend_key"), nullable=False)
#     status=db.Column(db.Boolean, default=False)
    

############

# def befriend(self, pal):
#     if pal not in self.pals:
#         self.pals.append(pal)
#         pal.pals.append(self)
    
# def unfriend(self, pal):
#     if pal in self.pals:
#         self.pals.remove(pal)
#         pal.pals.remove(self)

# def convert_pets_to_friends(self):
#          return {"friendship id": self.friendship_id, 
#                  "pal status": True}
############
# pending_pals = db.Table('pending_pals',
# db.Column('pet_id', db.Integer, db.ForeignKey('pet.id')),
# db.Column('added_pal', db.Integer, db.ForeignKey('pet.id')), 
# db.Column('status', db.Boolean, default=False, nullable=False), 
# )

# class Friendship(db.Model):
#    id = db.Column(db.Integer, primary_key = True)

#    pending_pals = db.relationship('Friendship', 
#         secondary = pending_pals, 
#         primaryjoin = (pending_pals.c.pet_id == id), 
#         secondaryjoin = (pending_pals.c.added_pal == id),
#         lazy = 'dynamic'
#     ) 
############
# from app import db
# from sqlalchemy import ForeignKey
# from sqlalchemy import UniqueConstraint
# from sqlalchemy.orm import relationship


# friendship = db.Table("Friendship",
#     db.Column('user_id', db.Integer, ForeignKey('users.id'), index=True),
#     db.Column('pal_id', db.Integer, ForeignKey('users.id')),
#     UniqueConstraint('user_id', 'pal_id', name='unique_friendships'))


# class User(db.Model):
#     __tablename__ = 'users'

#     pals = relationship('User',
#                            secondary=friendship,
#                            primaryjoin=id==friendship.c.user_id,
#                            secondaryjoin=id==friendship.c.pal_id)
    
    