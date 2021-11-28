# User_survey_system

This Survey API allows:
to create, edit, and delete surveys, questions and answer options through the admin panel;
get the list of surveys with questions and answer options;
take surveys;
get the list of answers with details on questions and surveys


## Used technologies

* [Django](https://djangodoc.ru/3.2/)
* [DRF](https://www.django-rest-framework.org/)


## Quick start

### Run project

```bash
git clone https://github.com/DaryaRu/User_survey_system.git
cd User_survey_system
python -m venv venv

# for Windows
source venv/Scripts/activate
# for Linux
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Project structure

```
root
|
| - config
| - survey
    |
    | - admin
    | - migrations
    | - models
    | - serializers
    | - viewsets
| manage.py
| README.MD
| requirements.txt
```