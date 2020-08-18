from pymongo import MongoClient

client = MongoClient("mongodb+srv://dev:nepal123@tulikaa.xf2my.mongodb.net/TulikaDB?retryWrites=true&w=majority")
tulika_db = client.get_database("TulikaDB")
users_collection =tulika_db.get_collection("users")
