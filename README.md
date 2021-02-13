## Group Portfolio App

**Setup and Run Locally**
---
*Requirements:- Python 3.8+*<br>
1) `git clone https://github.com/anonshubh/synergee.git`
(For Developer: Use your Forked URL) 
2) `cd synergee`
3) `python -m venv env`
4) `source env/bin/activate` (Mac/Linux)<br>
   `env/Scripts/activate.ps1` (Windows-Powershell)
5) `pip install -r requirements.txt`
6) `python manage.py runserver`

<br>

**Specifications**
<br>
1) New Members can be added to group in real-time via Synergee's Admin Panel. <br>
2) Every Member's interests can be added/modifed. <br>
3) Every Members can post their Blogs on their Interests. <br>
4) Contact-Us functionality enables the users to reach a individual group member or the entire team.<br>

**For Developers**
<br>
1) App contains two django apps - blog and group. <br>
2) "Group" app defines the addition/modification of new members. <br>
3) "Blog" app defines the blogs by individual group members. <br>
4) The Contact-Us functionality is implemented in "Group" app. <br>

***Tech Stack***
<br>
Client-Side: HTML5, CSS3, VanillaJS <br>
Server-Side: Django>=3.1.* <br>
Database: PostgreSQL 12 <br>
