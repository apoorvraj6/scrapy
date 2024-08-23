from pymongo import MongoClient
import datetime

client = MongoClient("mongodb+srv://rajapoorv858:QtQBvMvqcKASO3Ib@cluster0.aoigm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.scrapy
posts = db.test_collection

doc = post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
}

post_id = posts.insert_one(post).inserted_id