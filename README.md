# Five Rings
## Author
* [Shaggy](https://github.com/Dhyder)

## Description
Five Rings the Awwwards recreation.

## Screenshots
![Ring]()
![Ring]()
![Ring]()

## Live Link
You can view the site at: [Five Rings](https://fiverings.herokuapp.com/)

## User Story
- A user can view posted projects and their details.
- A user can post a project to be rated/reviewed.
- A user can rate/ review other users' projects.
- Search for projects.
- View projects overall score.
- A user can view their profile page.


## SetUp / Installation Requirements
### Prerequisites
* Django 2.2.24
* python3.8.10
* virtualenv
* pgAdmin4
* HTML5  
* CSS3
* Javascript 
* Font Awesome
* jQuery

### Cloning
* In your terminal:

        git clone https://github.com/Dhyder/Awwards.git
        cd Awwards/

## Running the Application
* Creating the virtual environment

        virtualvenv virtual
        source virtual/bin/activate
 or in (windows)
 
        source virtual/Scripts/activate

* Installing Dependencies

        pip install -r requirements.txt
        
* Making Migrations

        python manage.py makemigrations awwwards
        
* Migrate

        python manage.py migrate

* Running the application:

        python3.8 manage.py runserver
        

## Testing the Application
* To run the tests for the class files:

        python3.8 manage.py test
        
## My Api Endpoints
* [users](https://fiverings.herokuapp.com/api/users/)
* [profile](https://fiverings.herokuapp.com/api/profile/)
* [posts](https://fiverings.herokuapp.com/api/posts/)

## Technologies Used
* Python3.8.10
* Django2.2.24

## Known Bugs
* No known bugs at the moment
## Author's Contact Information
* For any queries, you can reach out at [desastrecaliente@gmail.com]

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)]()  
* Copyright (c) 2021 **Shaggy**
