# piazza_bot
A bot to create scheduled piazza posts. Feel free to reach out to jackhong@umich.edu for any questions.

---
Usage :

You need to set the following ENV variables first. These can be updated [here](https://github.com/organizations/eecs370/settings/secrets/actions)

`PIAZZA_EMAIL` : Should be an organization secret. I personally made a bot piazza account like `jackhong+PIAZZABOT@umich.edu` for the Piazza bot.

`PIAZZA_PASSWORD`: Should be an organization secret. This is the password for the bot account.

`PIAZZA_CLASS_ID` : If the current semester url is `https://piazza.com/class/l79dvmfeb8c49n`, then the CLASS_ID should be `l79dvmfeb8c49n`

TITLE : Title of the post

BODY : Body of the post, in a markdown format

PROJECT : The single subfolder of the 'project' folder you want to post to, ex: projet_1, project_2, project_3, project_4

<img width="839" alt="Screenshot 2023-08-31 at 11 38 21 AM" src="https://github.com/eecs370/piazza_bot/assets/46696737/c5fcb696-dc07-4cdb-b721-eae3383e5f4c">

*This was how the project folder structure was setup for F22*

$ piazza_bot.py

This repo needs to be public, as it is in the project spec repos which host github pages.
