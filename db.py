from pymongo import MongoClient

client = MongoClient("mongodb+srv://test:test@chatapp.cdjiv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

chat_db = client.get_database("chatdb")
users_collection = chat_db.get_collection("users")

def save_user(username,email,password):
    password_hash = generate_password_hash(password)
    users_collection.insert_one({'_id':username,'email':email,'password':password)

save_user("test123","test@mail.com","test")
