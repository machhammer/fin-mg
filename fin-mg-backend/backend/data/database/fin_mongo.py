import pymongo
import pprint



myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["fin-mg-database"]
user_col = db["users"]


def users():
    results = {}
    cursor = user_col.find()
    for i in cursor:
        print(type(i))
        if '_id' in i: del i['_id'] 
        results.update(i)
    return (results)

def user(username):
    print ("DATABASE search for user: " + username)
    user = user_col.find_one({'username': username})
    return user

if __name__ == '__main__':
    print("Database started")