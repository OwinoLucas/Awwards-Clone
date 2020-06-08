# Awwards Clone

> [Lucas](https://github.com/OwinoLucas)

# Description
This project allows users to post their projects for other users to rate according to design, usability and content.

## Live Link

Click [View Site](https://cloneawwards.herokuapp.com/) to visit the site

## Behavior Driven Development

| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| View posted projects | None | Display all projects |
| Authenticate users | text inputs | create a profile after reqistration and log in|
| Star rate a project| click a button| user leaves a rating based on options provided|

## Screenshots
* Home Page
![Screenshot from 2020-06-09 01-38-16](https://user-images.githubusercontent.com/60548928/84087131-2ec40700-a9f2-11ea-8340-974e3f0b218f.png)
* Projects page with ratings
![Screenshot from 2020-06-09 01-38-31](https://user-images.githubusercontent.com/60548928/84087140-32f02480-a9f2-11ea-8bca-4fd643456219.png)
* Profile page
![Screenshot from 2020-06-09 01-38-40](https://user-images.githubusercontent.com/60548928/84087146-34215180-a9f2-11ea-9f84-3f584129739e.png)
## User Story
- A user can view posted projects and their details.
- A user can post a project to be rated/reviewed.
- A user can rate/ review other users' projects.
- Search for projects.
- View projects overall score.
- A user can view their profile page.
## Setup and Installation

To get the project:

##### Cloning the repository:

```bash
https://github.com/default-007/awwwards.git
```

##### Navigate into the folder and install requirements

```bash
cd project-awwards pip install -r requirements.txt
```

##### Install and activate Virtual

```bash
- python3 -m venv virtual - source venv/bin/activate
```

##### Install Dependencies

```bash
pip install -r requirements.txt
```

##### Setup Database

SetUp your database User,Password, Host then make migrate

```bash
python manage.py makemigrations instagram
```

Now Migrate

```bash
python manage.py migrate
```

##### Run the application

```bash
python manage.py runserver
```

##### Testing the application

```bash
python manage.py test
```

Open the application on your browser `127.0.0.1:8000`.

### Api Endpoints

## Technical Requirements
* Create a specs markdown file that lists down all the projects specifications.
* All your models should contain unit tests to test the different behaviours. All your test should pass.
* Your project should follow the proper folder structure.
* Your project should be deployed to Heroku.
* Your project should contain proper commit messages.

## Technology used

- [Python3.6.9](https://www.python.org/)
- [Django 3.0.6](https://docs.djangoproject.com/en/2.2/)
- [Heroku](https://heroku.com)


## Contact Information

If you have any question or contributions, please email me at [lucowish35@gmail.com]

## License
Copyright (c) [2020] [Lucas Otieno]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.