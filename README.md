<img src="/portal/static/branding/logo.png" alt="LIVE Portal" width="220px"/>

## Description of the Portal
A web application used by both delegates and partners during LIVE Competition in 2019. This application is sponsored and powered by Microsoft Azure.

### The Gist of Each Role in Portal
Here are lists of basically what partners, delegates, judges, and executives can do.

**Partners are able to:**
- View widgets in the "What's New" section
- View all delegates and filter them by school, seeking status, and year of study
- View all teams and their ranking in the competitions (when released)
- View rounds that are set visible by an Executive, and each of teams' submissions to those rounds, as well as videos of their presentations
- View contact details of LIVE members
- View the itinerary

**Delegates are able to:**
- View widgets in the "What's New" section
- View their team
- View everything corporate (corporate individuals and organizations participating in the competition)
- View/upload rounds
- Ask questions and view questions (and their answers) raised by other delegates
- View contact details of LIVE members
- View the itinerary

**Judges are able to:**
- Judge rounds (make assessments for an assigned round and team)
- View the itinerary
- View contact details of LIVE members

**Executives are able to:**
- Add/change the list of corporate individuals and organizations
- Add/change the itinerary (days, events)
- Add/change the list of LIVE Executives (aside: code under contacts folder)
- Add/change the image or text widgets in the "What's New" section
- Send text messages to all Delegates with phone numbers
- Answer questions raised by Delegates
- Ask questions, and answer them
- Add/change rounds and rubrics (one rubric has one round)
- Assign assessments (an assessment is an evaluation of a round, per team) to each judge (should be done after the rubric is finalized)
- View assessments by judges and export the assessments as an excel file
- Add/change videos of presentations per team for each round
- Create Teams, Partner Users, Delegate Users, Judge Users, Executive Users

## Prerequisites
- Python - v3.7.0
- pip - v18.1
- Django - v2.1.2 (in requirements.txt)
- twilio - v6.20.0 (in requirements.txt)
- Pillow - v5.3.0 (in requirements.txt)
- hashids - v1.2.0 (in requirements.txt)
- django-storages v1.7.1 (in requirements.txt)
- azure-storage-blob - v1.4.0 (in requirements.txt)
- pyodbc - v4.0.24 (in requirements.txt)
- django-pyodbc-azure - v2.1.0.0 (in requirements.txt)
- django-import-export - v1.1.0 (in requirements.txt)
- openpyxl - v2.4.9 (in requirements.txt)
- django-tinymce - v2.7.0 (in requirements.txt)

## The Build (on Windows)
These are instructions for a development environment:
1. Open up PowerShell on Windows
2. Clone the repository
`$ git clone https://github.com/alvintangz/live-portal.git`
3. Enter a virual environment (instructions are for windows machine below) - Optional
`$ python3 -m venv env`
`$ env\Scripts\activate`
4. Install all the required modules listed in requirements.txt
`$ pip install -r requirements`
5. Add environment variables
Environment variables are used to store very sensitive data. Learn more: official [Django Documentation - Django settings]([https://docs.djangoproject.com/en/2.1/topics/settings/#security).
- LP_DB_NAME: Default database name. *Default database is using Microsoft SQL Server.*
- LP_DB_USER: Default database user. *Default database is using Microsoft SQL Server.*
- LP_DB_PASSWORD: Default database password. *Default database is using Microsoft SQL Server.*
- LP_DB_HOST: Default database host. *Default database is using Microsoft SQL Server.*
- LP_DB_PORT: Default database port. *Default database is using Microsoft SQL Server.*
- LP_EMAIL_HOST: Default email host. *Default email settings is using a SMTP Backend with a SendGrid plan.*
- LP_EMAIL_PORT: Default email port. *Default email settings is using a SMTP Backend with a SendGrid plan.*
- LP_EMAIL_PASSWORD: Default email password. *Default email settings is using a SMTP Backend with a SendGrid plan.*
- LP_TWILIO_SID: sid for Twilio.
- LP_TWILIO_TOKEN: token for Twilio.
- LP_TWILIO_NUMBER: number for Twilio.
- LP_SALTONE: A random salt.
- LP_SALTTWO: A random salt.
- LP_AZURE_STORAGE_KEY: Azure Account Key for blob storage.
6. Make migrations - Optional (for easy extending)
`$ python manage.py makemigrations`
7. Migrate
`$ python manage.py migrate`
8. Create a superuser
`$ python manage.py createsuperuser` and follow prompts
9. Run development server
`$ python manage.py runserver`

## Owners
These parties have access to use the files in this project as they please.
* Alvin Tang (IT Solutions Manager at LIVE 2018-2019 // Developer of LIVE Portal)
* LIVE Competition (https://live-competition.org/)

## License
The files under this project does not have a license. As such, these files are not free to distribute and use unless you have written consent from all owners. If you do have such consent, feel free to look at the [extending document](extending.md) for ways to extend the existing application.

## Acknowledgments
* Argon Dashboard - [Github Repository](https://github.com/creativetimofficial/argon-dashboard)
* Django - [Github Repository](https://github.com/django/django)
* Django Multiple User Types Example - [Github Repository](https://github.com/sibtc/django-multiple-user-types-example)
