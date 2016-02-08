import json
from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost', 27017)

def insert():
  input_json = """
{
    "Wall": [
        {
            "Wall_id": "wall001",
            "user_id": "user001",
            "message_author": "AuthorD",
            "wall_message": "content:TRY",
            "posted_on": "24/8/15",
            "author_id": "A004",
            "path_to_files": "[home/path]",
            "wall_recepients": "[user001,user002]",
            "time_stamp": "878433774394",
            "Comments": [
                {
                    "comment_id": "cmt001",
                    "Wall_id": "wall001",
                    "user_id": "user001",
                    "pathtofile": "[home/doc/file]",
                    "comment": "try 2",
                    "profile_pic": "home2/pic.jpg",
                    "user_name": "user2",
                    "timestamp": "98546272222",
                    "comment_reply": [
                        {
                            "reply_id": "rly001",
                            "comment_id": "cmt001",
                            "user_id": "user003",
                            "pathtofile": "[home/doc/file]",
                            "reply": "try 4",
                            "profile_pic": "home2/pic.jpg",
                            "user_name": "user",
                            "timestamp": "98546272222"
                        }
                    ]
                }
            ]
        }
    ]
}
      """

  return input_json

if __name__ =="__main__":

    con = MongoClient()

    db = client['sampledb']
    posts = db["posts"]

    wall = json.loads(insert())
    posts.insert_one(wall) 

    print "insert sucessful"
