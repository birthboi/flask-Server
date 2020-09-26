"# flask-Server" 
Ok. So hey. You downloaded it. Nice.

First thing, when setting this up..

Go to cortona/search bar and search env.
Press enter as soon as a computer icon pops up.

Click 'Enviroment Variables'
Set an enviroment variable named **SQLALCHEMY_DATABASE_URI** to sqlite:///site.db

Keep the window open but open up command line.

In command line do:

*C:/Users/**usernamehere**/> python*

A python interperator should open up. Input the following command.

*>>>import secrets*
*>>>secret = secrets.token_hex(16)*
*>>>secret* or *>>>print(secret)*

The secret will be printed.

Copy it and go back to the enviorment variables window.

Make a new enviroment variable called **SECRET_KEY** and paste the secret key inside.

Last thing, open the 'meow' folder and type *cmd* in the path bar.

Type the following command.

*C:/Users/**usernamehere**/> pip install -r requirements.txt*

After it installs do

*C:/Users/**usernamehere**/> python run.py*