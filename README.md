# My Django_Website 

A complete and fully implementable software for a company to ease out the work of HR's. Now no need to maintain huge excel sheets to store information about fields like candidates, companies, job openings and stuff. Every thing is made easier through create, update and delete forms and the data is displayed in the form of tables from the database. The data can also be uploaded through csv files. Different privileges are given to the admin and staff users. The website also has a unique tracker for each logged in user where the person can keep track, schedule interviews and send auto-generated emails to his/her respective candidates. 

# Technology Stack

* Front-end - HTML, CSS, Bootstrap (Django template)
* Back-end - Django framework
* Database - PostgreSQL


## 🔧 Instructions to run
```
git clone https://github.com/amyy28/Django-website.git
```

### In the cloned repository
Execute 
```
cd wise_intern
```

### Install all the requirements at once
```
pip3 install -r requirements.txt
```

### Create a superuser for login
Create your username and password of your choice
```
python3 manage.py createsuperuser
```

### Now you require to migrate all the database table schemas to the default sql database 
```
python3 manage.py makemigrations
```

### Migrate it
```
python3 manage.py migrate
```

### Now run the server
```
python3 manage.py runserver
```

## Hit the below URL
```http://127.0.0.1:8000/```

Now go to login and enter the created username and password. Once logged in, create the team by filling in the required details and then skit and presentations data can easily be loaded using the forms in the UI. 

### 💁🏻 Contributing
Any contributions and pull requests are welcomed! 

### Made with :heart:

