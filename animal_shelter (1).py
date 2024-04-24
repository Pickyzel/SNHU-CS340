from pymongo import MongoClient
from bson.objectid import ObjectId
class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self,username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32201
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
# Create(C in CRUD)
    def create(self, data):
        if data is not None:
            try:
                createdDoc = self.database.animals.insert_one(data)# data should be dictionary 
                return True
            except Exception:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
# Read(R in CRUD).
    def read(self, data):
        if data is not None:
            findData = self.database.animals.find(data)
        else:
            raise Exception("Nothing to save, because data parameter is empty")
        return findData
        
# Update(U in CRUD)
    def update(self, read, data):
        if data is not None:
            updateData = self.database.animals.update_many(read, {"$set": data})
            return updateData.modified_count
        else:
            raise Exception("Nothing to save, because data parameter is empty")
    
# Delete(D in CRUD)
    def delete(self, data):
        if data is not None:
            deletedData = self.database.animals.delete_many(data)
            return deletedData.deleted_count
        else:
            raise Exception("Nothing to save, because data parameter is empty")
