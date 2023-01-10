import os
import sys

from piazza_api.piazza import PiazzaRPC

class PiazzaBot(object):
    
    def __init__(self, class_id):
        self.rpc = PiazzaRPC(class_id)
        self.rpc.user_login(os.getenv("PIAZZA_EMAIL"), os.getenv("PIAZZA_PASSWORD"))
        self.network_id = class_id

    def make_note(self, subject, markdown_content, folder):
        dirs = ["p1asm", "p1sim", "p1mult"]

        params = {"nid":self.network_id,"type":"note","subject":subject,"content":markdown_content,"anonymous":"no","client_time":"8/26/2022, 7:08:39 PM","status":"active","folders":dirs,"config":{"is_announcement":1,"bypass_email":1},"prof_override":True}

        self.rpc.content_create(params)
       
if __name__ == '__main__':    
    poster = PiazzaBot(os.getenv("PIAZZA_CLASS_ID"))
    poster.make_note(os.getenv("TITLE"), os.getenv("BODY"), os.getenv("FOLDER"))
