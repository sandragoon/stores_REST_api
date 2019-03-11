from flask_restful import reqparse, Resource
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument (
                            "price",
                            type = float,
                            required = True,
                            help = "This field can't be left blank!"
                        )
    parser.add_argument (
                        "store_id",
                        type = str,
                        required = True,
                        help = "This field can't be left blank!"
                        )


    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message" : "item not found"}, 404

    @jwt_required()
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message':"An item named {} already exists!".format(name)}, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, **data)
        try:
            item.save_to_db()
        except: return {"message" : "An error occured inserting the item "}, 500

        return item.json(), 201 #201 is for "he request has been fulfilled and resulted in a new resource being created."

    @jwt_required()
    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            ItemModel.delete_from_db(item)
            return {'message' : 'item has been deleted'}
        return {'message' : 'item not found!!!'}

    @jwt_required()
    def put(self, name):

        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data['price']
        item.save_to_db()
        return item.json(), 201

class ItemList(Resource):
    def get(self):
        return {'items list':list(map(lambda item : item.json(), ItemModel.query.all()))}
