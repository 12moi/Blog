


# Blog

## Author
Moi Shadrack

### Description
This is a flask application that allows writers to post blogs, edit and delite blogs. It also allows users who have signed up to comment on the blogs that has been posted by a writer. It also allows a person to subscribed to recieve email everytime a new blog is posted by a writer.

### User Story
. A user can view the most recent posts.<br>
. View and comment the blog posts on the site.<br>
. A user should an email alert when a new post is made by joining a subscription.<br>
. Register to be allowed to log in to the application<br>
. A user sees random quotes on the site<br>
. A writer can create a blog from the application and update or delete blogs I have created.

### Development Installation
To get the code..<br>

1. Cloning the repository:<br>
https://github.com/12moi/Blog.git<br>

2. Move to the folder and install requirements<br>
cd Blog<br>
pip install -r requirements.txt<br>
3. Exporting Configurations<br>
export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}<br>
4. Running the application<br>
python manage.py server<br>
5. Testing the application<br>
python manage.py test<br>
Open the application on your browser 127.0.0.1:5000.

### Technology used
Python3.6<br>
Flask<br>
Heroku.

### Known Bugs
There are no known bugs currently but pull requests are allowed incase you spot a bug.

### Contact Information
If you have any question or contributions, please email me at [moi.shadrack@student.moringaschool.gmail.com]

#### License
MIT License:
Copyright (c) 2022 Moi Shadrack