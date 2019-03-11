from db import db

class UserModel(db.Model):

    # giving table name which is same as the table name in database
    __tablename__ = "users"

    # creating columns with threre specific type and limit on the length
    id = db.Column(db.Integer, primary_key = True) # primary key means entry in the cloumn is unique in the database
    username = db.Column(db.String(80)) #data entering sholud not be grater than length of 80
    password = db.Column(db.String(80))


    def __init__(self, username, password ):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username = username).first() #select * from __tablename__ where name =name LIMIT 1


    @classmethod
    def find_by_user_id(cls, _id):
        return cls.query.filter_by(id = _id).first() #select * from __tablename__ where user_id= _if LIMIT 1
