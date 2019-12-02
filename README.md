# Neighborhood Watch

## Description
Neighborhood Watch is a django application used to display location information for resisdents.
It helps in users find basic services in their location.  

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I can:

* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display Login Page | **On page load** | Login Page |
| Display Home Page  | **Correct Login Credentials** | Home Page|
| View hood details | **Click the 'Location Feed' tab on the Navbar** | Hood posts, businesses and public services|
| Manage Profile |**Click 'Accounts' then 'Profile' on Navbar**|Displays user profile and options to manage user profile|



## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* postgres database
* virtualenv
* django

### Cloning
* In your terminal:
        
        $ git clone https://github.com/sokkyyy/hood-watch.git
        $ cd project-ranker

## Running the Application
* Creating the virtual environment:

        $ pip install virtualenv
        $ virtualenv virtual
        $ source virtual/bin/activate

* Installing Django and other Modules:

        $ pip install -r requirements.txt


* To run the application, in your terminal:


        $ python3.6 manage.py runserver



## Testing the Application
* To run the tests for the class files:

        $ python3.6 manage.py test project

## Technologies Used
* Python3.6
* Django
* Semantic UI
* Postgres SQL

## License
[Ray Ndegwa](https://github.com/sokkyyy/)
