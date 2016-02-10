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
            "message_author": "AuthorA",
            "wall_message": "content:TRY",
            "posted_on": "24/8/15",
            "author_id": "A001",
            "path_to_files": "[home/path]",
            "wall_recepients":"[user001,user002,user003,user004,user005]",
            "time_stamp": "561651561552",
            "Comments": [
                {
                    "comment_id": "cmt001",
                    "Wall_id": "wall001",
                    "user_id": "user001",
                    "pathtofile": "[home/doc/file]",
                    "comment": "try 2",
                    "profile_pic": "home2/pic.jpg",
                    "user_name": "user2",
                    "timestamp": "8975616544515",
                    "comment_reply": [
                        {
                            "reply_id": "rly001",
                            "comment_id": "cmt001",
                            "user_id": "user002",
                            "pathtofile": "[home/doc/file]",
                            "reply": "try 4",
                            "profile_pic": "home2/pic.jpg",
                            "user_name": "user",
                            "timestamp": "91877798442158"
                        }
                    ]
                },
                {
                    "comment_id": "cmt002",
                    "Wall_id": "wall001",
                    "user_id": "user002",
                    "pathtofile": "[home/doc/file]",
                    "comment": "try 2",
                    "profile_pic": "home2/pic.jpg",
                    "user_name": "user2",
                    "timestamp": "6484798454984",
                    "comment_reply": [
                        {
                            "reply_id": "rly002",
                            "comment_id": "cmt002",
                            "user_id": "user003",
                            "pathtofile": "[home/doc/file]",
                            "reply": "try 4",
                            "profile_pic": "home2/pic.jpg",
                            "user_name": "user",
                            "timestamp": "198782789445"
                        }
                    ]
                }
            ]
        },
        {
            "Wall_id": "wall002",
            "user_id": "user002",
            "message_author": "AuthorB",
            "wall_message": "content:TRY",
            "posted_on": "24/8/15",
            "author_id": "A002",
            "path_to_files": "[home/path]",
            "wall_recepients":"[user002,user003,user004,user005,user006]",
            "time_stamp": "984298429842",
            "Comments": [
                {
                    "comment_id": "cmt001",
                    "Wall_id": "wall001",
                    "user_id": "user001",
                    "pathtofile": "[home/doc/file]",
                    "comment": "try 2",
                    "profile_pic": "home2/pic.jpg",
                    "user_name": "user2",
                    "timestamp": "548494511685",
                    "comment_reply": [
                        {
                            "reply_id": "rly001",
                            "comment_id": "cmt001",
                            "user_id": "user003",
                            "pathtofile": "[home/doc/file]",
                            "reply": "try 4",
                            "profile_pic": "home2/pic.jpg",
                            "user_name": "user",
                            "timestamp": "695498414+9844"
                        }
                    ]
                }
            ]
        },
        {
            "Wall_id": "wall003",
            "user_id": "user003",
            "message_author": "AuthorC",
            "wall_message": "content:TRY",
            "posted_on": "24/8/15",
            "author_id": "A003",
            "path_to_files": "[home/path]",
            "wall_recepients":"[user003,user004,user005,user006,user007]",
            "time_stamp": "6549845498484"         
        }    
    ]
}
      """

  return input_json

if __name__ =="__main__":

    con = MongoClient()

    db = client['sampledb']
    post = db["post"]

    wall = json.loads(insert())
    post.insert_one(wall) 

    print "insert sucessful"

    recepients = db.post.distinct("Wall.wall_recepients")
    print(recepients)

    


