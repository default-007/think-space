# think-space

[think-space](https://think-space07.herokuapp.com/)

#### By **[Brian Otieno](https://github.com/default-007)**

## Description

A personal blogging website where users post and share their blogs with other users.

Logged in users have their profile page where they can view the blogs they posted and see comments made. One can delete a comment, and a blog as well.

The application uses postgres sql database to store the various blogs and information in the website. WTF flask forms are heavily in use.

Project is then deployed to heroku

## Behaviour Driven Development

| Input                |                                    Output                                     |                                                                       Behavior |
| -------------------- | :---------------------------------------------------------------------------: | -----------------------------------------------------------------------------: |
| Visit Think Space    |                         Various quotes are displayed                          |                                            User can only view the daily quotes |
| Sign in              |                     Application sends a welcoming message                     |                                                            User has an account |
| Trash can icon       | A comment or a post is deleted only if the user is the owner of the blog post | A blog post or a comment is deleted if the user is the owner of the blog poast |
| Click on create blog |              Application displays a form for you to post a blog               |                                                   Submit to save blog is saved |
| Subscribe...         |                                     None                                      |                                                                 app send email |
| Sign out             |                            Home page is displayed                             |                                                  leaves current logged in user |
| Visit profile        |                           Profile details displayed                           |                                user can edit their bio or upload profile photo |

## Live link

https://think-space07.herokuapp.com/

## ScreenShots

## Set-up instructions and installations

- Navigate to the projects folder then run `python3 -m venv virtual`
- Go virtual `source virtual/bin/activate` You need to have the following installed
- Flask pip install flask
- Flask-script pip install flask-script
- Flask-bootstrap pip install flask-bootstrap you could still use the bootstrap cdn
- Flask-login pip install flask-login for user authentication
- Flask migrations are necessary for us to update our database

- Run `python3.6 manage.py db init` to initialize your migrations.
- Run `python3.6 manage.py db migrate -m "message"` for every migration required.
- Run `python3.6 manage.py db upgrade` to upgrade your database migrations.
- Ensure to have the correct folder structure to minimize errors

### Prerequsites

    - Python 3 or later version
    - pip
    - flask

### Clone the Repo

Run the following command on the terminal:
`https://github.com/default-007/think-space.git`

Install [Postgres](https://www.postgresql.org/download/)

### Create a Virtual Environment

Run the following commands in the same terminal:
`sudo apt-get install python3.6-venv`
`python3.6 -m venv virtual`
`source virtual/bin/activate`

### Install dependancies

Install dependancies that will create an environment for the app to run
`pip3 install -r requirements`

### Prepare environment variables

```bash
export DATABASE_URL='postgresql+psycopg2://username:password@localhost/pitchit'
export SECRET_KEY='Your secret key'
```

### Run Database Migrations

```
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
```

### Running the app in development

In the same terminal type:
`python3 manage.py server`

Open the browser on `http://localhost:5000/`

## Known bugs

`None so far but i'll be glad to be communicated to if there is one`

## Technologies used

    - Python 3.6
    - HTML
    - Bootstrap 4
    - Animate CSS
    - Heroku
    - Postgresql

## Support and contact details

Contact me on brianokola@gmail.com for any comments, reviews or advice.

### License

Copyright (c) **Brian Otieno**
