<img src="/portal/static/branding/logo.png" alt="LIVE Portal" width="220px"/>

## Description of the Portal
A web application used by both delegates and partners during LIVE Competition in 2019. This application is sponsored and powered by Microsoft Azure.

Partners will be able to:
- View the President’s message
- View delegates
- View teams
- View rounds
- View contact details of important LIVE members

Delegates will be able to:
- View the President’s message
- View their team
- View everything corporate
- View/upload rounds
- View contact details of important LIVE members
- Send feedback
- View itinerary

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

## The Build (on Windows)
The production environment is built on a Docker image. These are instructions on development:
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

## Owners
These parties have access to use the files in this project as they please.
* Alvin Tang (IT Solutions Manager at LIVE 2018-2019 // Developer of LIVE Portal)
* LIVE Competition (https://live-competition.org/)

## License
The files under this project does not have a license. As such, these files are not free to distribute and use unless you have written consent from all owners.

## Acknowledgments
* Argon Dashboard - [Github Repository](https://github.com/creativetimofficial/argon-dashboard)
* Django - [Github Repository](https://github.com/django/django)
* Django Multiple User Types Example - [Github Repository](https://github.com/sibtc/django-multiple-user-types-example)
