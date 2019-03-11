from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        else:
            return {"message" : "store not found"}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"messgae" : "store is already there"}
        store = StoreModel(name)
        try :
            StoreModel.save_to_db(store)
        except :
            return {"message" :"an error ocurred while storing"}

        return store.json()

    def delete(self, name):
        store  = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {"message" : "store has been deleted"}
        return {"messgae" : "store not found"}


class StoreList(Resource):
    def get(self):
        return {'stores': list(map(lambda x: x.json(), StoreModel.query.all()))}
