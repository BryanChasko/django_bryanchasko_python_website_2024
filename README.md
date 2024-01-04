Bryanchasko Django Web App
This repository contains the source code for the Bryanchasko website, built using Django and Python. 🌐✨

How This Project Was Made

Setting Up the Development Environment
Create Local Directory:
Open a terminal and create the project directory:
mkdir bryan_chasko_django_app && cd bryan_chasko_django_app

Python 3 Check:
Verify Python 3 installation:
python3 --version

If not installed, use your system's package manager to install python3. (e.g., on macOS, use brew install python3)

Install Pip if Needed: 
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
or sudo apt install python3-pip

Virtual Environment: A Realm for Isolation 🛡️
Create a virtual environment to keep dependencies separate:

python3 -m venv venv_bryanchasko_django_website
source venv_bryanchasko_django_website/bin/activate

Django's Arrival
Install Django: 🚀
Install Django within the activated virtual environment:

pip install django
Creating a New Project: 🎉
Create a new Django project named "bryan_chasko_django_app":

django-admin startproject bryan_chasko_django_app
cd bryan_chasko_django_app
Desired Directory Structure 📁
plaintext

bryan_chasko_django_app/
├── venv_bryanchasko_django_website/ (virtual environment)
└── bryan_chasko_django_app/ (Django project)
   ├── manage.py (command center)
   └── bryan_chasko_django_app/ (project files)
      ├── __init__.py
      ├── settings.py (configuration hub)
      ├── urls.py (routing map)
      └── asgi.py & wsgi.py (server gateways)

Creating Your Secrets & Keeping Them Separate/out of Git | Creating Your Secret Key:
Creating a Secret Key:
In your terminal from your Django project directory (bryan_chasko_django_app/), while activated in the virtual environment, run:
python3 manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

Copy the generated key and paste it into the SECRET_KEY in settings.py.

Creating a .env File:
Create a file named .env in the root directory of your Django project (bryan_chasko_django_app/bryan_chasko_django_app/). Define your secret key using the following syntax:
SECRET_KEY=your_super_secret_key_here

Installing python-dotenv:
Install the python-dotenv package in your virtual environment:
pip install python-dotenv
Loading Secrets from the Vault:

At the top of your settings.py file, add these lines to load variables from .env:
from dotenv import load_dotenv
load_dotenv()  # Loads environment variables from .env file
SECRET_KEY = os.getenv("SECRET_KEY")  # Retrieves the secret key from the environment

Keeping the Secrets Secret: 🤫
Add .env to your .gitignore file to prevent it from being committed to version control.

Running This Project
Setting Up the Development Environment
Clone the repository.

Create a virtual environment and activate it.

Install dependencies:
pip install -r requirements.txt
Running the Development Server

python3 bryan_chasko_django_app/manage.py runserver
Access the development server at http://127.0.0.1:8000/.

.env File and Git Configuration
Ensure to create a .env file inside bryan_chasko_django_app/bryan_chasko_django_app/ to store sensitive information like the SECRET_KEY. Exclude the .env file and the virtual environment folder (venv_bryanchasko_django_website/) from version control using .gitignore.

Troubleshooting
If encountering issues like an empty SECRET_KEY or server errors, ensure the .env file is correctly set up and the environment variables are properly loaded.

Next Steps
After setting up the project and running the development server, here are the next steps to consider:

Create Templates: Develop HTML templates inside the bryan_chasko_django_app/bryanchasko_website/templates/bryanchasko_website/ directory for rendering the website content.

Static Files: If required, create a static directory inside the app directory (bryanchasko_website) to store CSS, JavaScript, or image files.

Deployment Preparation: Plan for deploying the application on Amazon S3 by converting Django templates to static HTML and configuring AWS services.

Database Configuration: Replace SQLite with PostgreSQL on Aurora Serverless v2 for the production environment.

Contribution
Contributions to improve the project are welcome! Please fork the repository, create a new branch, make your changes, and submit a pull request.

License
This project is licensed under the MIT License. feel free to hack it up.
