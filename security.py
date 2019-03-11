from models.user import UserModel
from werkzeug.security import safe_str_cmp #fucntion is used for safe string comaparison irrespective of python version
                                            #and irrespective of encodings such has utf-8, ascii etc

def authenticate(username, password):
    user  =  UserModel.find_by_username(username)#.get returns the value of ket 'username' or if key not found then None
    if user  and safe_str_cmp(user.password,password):
        return user

def identity(payload):
    user_id= payload['identity']
    return UserModel.find_by_user_id(user_id)
