import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
                        "username",
                        type = str,
                        required = True,
                        help = " username has to be entered"
                        )
    parser.add_argument(
                        "password",
                        type = str,
                        required = True,
                        help = "Password has to be given"
                        )
    @classmethod
    def post(cls):
        data = cls.parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {"message" : "A user with that name already exists"}

        user = UserModel(**data)
        UserModel.save_to_db(user)

        return {"message" : "{} user created sucessfully.".format(data["username"])}, 201
