# piazza_bot
A bot to create scheduled piazza posts


Usage :

You need to set the following ENV variables first

PIAZZA_EMAIL : Should be an organization secret

PIAZZA_PASSWORD: Should be an organization secret

PIAZZA_CLASS_ID : Class ID of the class you want to post to, this is public, but I have it as an org secret to make it easier to consume the variable.

Make sure to update these at : https://github.com/organizations/eecs370/settings/secrets/actions



     
TITLE : Title of the post

BODY : Body of the post, in a markdown format

PROJECT : The single subfolder of the 'project' folder you want to post to, ex: projet_1, project_2, project_3, project_4

$ piazza_bot.py
