from flask import  Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False #SQLALCHEMY_TRACK_MODIFICATIONS is set off to flask_alchemy to
app.secret_key = 'Santhosh'                            # track modifications in database
api = Api(app)

#using JWT
jwt = JWT(app, authenticate, identity) #jwt creates a new end point and the end point is
                                        # https:127.0.0.1:5000/auth
                                        #jwt runs auntenticate function and generate a encoded unique jwt string
                                        #for a given username and password
                                        #auth endpoint returns a Json Web token(jwt) unique for a given users
                                        #using jwt token it gets a user_id in identity and user details
#jwt_required is used has a decorator for given function has an auntication

#creating database
@app.before_first_request
def create_tables():
    db.create_all()

#creating end points
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister,'/register')

if __name__=='__main__':
    from db  import db
    db.init_app(app)
    app.run(port = 5000, debug = True)
