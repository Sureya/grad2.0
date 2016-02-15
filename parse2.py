
import json
from pymongo import MongoClient
from pymongo import DESCENDING

client = MongoClient('localhost', 27017)


def one():
    return {
                "Wall_id": "wall001",
                "user_id": "user001",
                "message_author": "AuthorA",
                "wall_message": "content:TRY",
                "posted_on": "24/8/15",
                "author_id": "A001",
                "path_to_files": "[home/path]",
                "wall_recepients":["user001","user002","user003","user004","user005"],
                "w_timestamp": 10,
                "Comments": [
                    {
                        "comment_id": "cmt001",
                        "Wall_id": "wall001",
                        "user_id": "user001",
                        "pathtofile": "[home/doc/file]",
                        "comment": "try 2",
                        "profile_pic": "home2/pic.jpg",
                        "user_name": "user2",
                        "c_timestamp": 15
                    }
                ]    
            }


def two():
    return {
    "Wall_id": "wall002",
    "user_id": "user002",
    "message_author": "AuthorB",
    "wall_message": "content:TRY",
    "posted_on": "24/8/15",
    "author_id": "A002",
    "path_to_files": ["home/path"],
    "wall_recepients":["user002","user003","user004","user005","user006"],
    "w_timestamp": 678,
    "Comments": [
        {
            "comment_id": "cmt001",
            "Wall_id": "wall001",
            "user_id": "user001",
            "pathtofile": "[home/doc/file]",
            "comment": "try 2",
            "profile_pic": "home2/pic.jpg",
            "user_name": "user2",
            "c_timestamp": 700
       },
        {
            "comment_id": "cmt001",
            "Wall_id": "wall001",
            "user_id": "user001",
            "pathtofile": "[home/doc/file]",
            "comment": "try 2",
            "profile_pic": "home2/pic.jpg",
            "user_name": "user2",
            "c_timestamp": 1000
       }
    ]
}



if __name__ =="__main__":

    db = client['grad']
    post = db["post"]

    insert = False

    if(insert):
        post.insert_one(one()) 
        print "1 done"
        
        post.insert_one(two()) 
        print "2 done"
        
    searchUser = "user002"
    result = post.find({"wall_recepients":{"$in":[searchUser]}}).sort([["post.w_timestamp",DESCENDING],["post.Comments.c_timestamp",DESCENDING]])
    ##result = post.find({"post.Comments.c_timestamp":{"$gt":16}})
    seen = False    
    for row in result:
        seen = True
        del row["_id"]
        print json.dumps(row, sort_keys=True, indent=4, separators=(',', ': '))
        print "\n\n"


    if not seen:
        print "Empty Result " 
