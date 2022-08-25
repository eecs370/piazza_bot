import os
import sys

from piazza_api.piazza import PiazzaRPC

class PiazzaBot(object):
    
    def __init__(self, class_id):
        self.rpc = PiazzaRPC(class_id)
        self.rpc.user_login(os.getenv("PIAZZA_EMAIL"), os.getenv("PIAZZA_PASSWORD"))
        self.network_id = class_id

    def make_note(self, subject, markdown_content, folder):
       
        path = ""

        dirs = []

        for subdir in folder.split("/"):
            path += subdir
            dirs.append(path)
            path += "/"
            
        config = {"is_announcement": 1, "bypass_email": 1}

        params = {"nid":self.network_id,"type":"note","subject":subject,"content":markdown_content,"anonymous":"no","client_time":"5/29/00 5:29 PM","status":"active","editor":"md","folders":dirs,"config":config}


        self.rpc.content_create(params)
       
if __name__ == '__main__':    
    poster = PiazzaBot(os.getenv("PIAZZA_CLASS_ID"))
    poster.make_note(os.getenv("TITLE"), os.getenv("BODY"), os.getenv("FOLDER"))
