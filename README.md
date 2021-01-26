# Django API-First Boilerplate

This repository is for generating template Django API projects for fast development. This includes integration of Django REST Framework (DRF) - https://www.django-rest-framework.org/. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

1. **Installing PostgresSQL (v10.0+)** - For this project we will be using PostgresSQL as our primary database. - [Link Here](https://www.pgadmin.org/download/)
2. **Installing PgAdmin (Optional)** -  It is suggested to install this or other alternative PostgresSQL Administration Tool - [Link Here](https://www.pgadmin.org/download/)
3. **Installing Python (v3.3+)** - The Django Web Framework is based on Python Programming Language - [Link Here](https://www.python.org/downloads/)

### Installing

To run the application you need to make sure that the prerequisites is already installed in your local machine.

Once that is finished, It is recommended to create a Python virtual environment to isolate packages required by this project from the main environment to prevent any breaking changes to your other python projects. You can know more about python virtual environments [here](https://realpython.com/python-virtual-environments-a-primer/) 

After all of that is settled, you can install the required python packages by running this in the project root directory 

```
pip install requirements.txt
```

then to run the Django Web Application, simply run this on the project root directory

```
python manage.py runserver
```

You should be seeing a status similar to this once the program is started

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 20, 2021 - 04:44:42
Django version 3.1.5, using settings 'django_boilerplate.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Kyle Aquino** - *Author* - [Kyle Aquino](https://github.com/kyleaquino)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* 
