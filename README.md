# piazza_bot
A bot to create scheduled piazza posts


Usage :

You need to set the following ENV variables first

PIAZZA_EMAIL : Should be an organization secret
PIAZZA_PASSWORD: Should be an organization secret

PIAZZA_CLASS_ID : Class ID of the class you want to post to
      The class ID is the portion of the url after /class/ -> https://piazza.com/class/kxwbis134cr64p = == kxwbis134cr64p
     
TITLE : Title of the post

BODY : Body of the post, in a markdown format

FOLDER : The single folder you want to post to, ex: P1, P2, P3...

$ piazza_bot.py
