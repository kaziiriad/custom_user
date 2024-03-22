# Custom Authentication For Django.

### Working With Django? Need User Authentication?
### No Need To Write The Same Old Code Again and Again. Use This Instead!


## User Guide

Everything is ready to roll. Just add your app folder inside the project or start a new one with the following command:

```bash
pip install -r requirements.txt
```

```bash
python manage.py startapp <your_app_name>
```
And add it to the `settings.py` file.

```python
INSTALLED_APPS = [
    'accounts',
    'guest_user',
    <your_app_name>
]
```
Add `.env` file to the root of your project.

Add `SECRET_KEY` variable to the the `.env` file. 
```python
SECRET_KEY=your_secret_key
```

Finally, run the following command:
```python
python manage.py migrate
```
---
### Or If You Want To Add It To Your Own Project. Follow The Following Instructions:

Install requirements.txt.
```bash
pip install -r requirements.txt
```

Copy the `accounts` folder and paste it to your project. 

Install them on your project as well as the `guest_user` module for Guest-Login functionality.
```python
INSTALLED_APPS = [
    ...
    'accounts',
    'guest_user',
    ...
]
```
Add the following line into the `AUTHENTICATION_BACKENDS`

```python
AUTHENTICATION_BACKENDS = [
   "django.contrib.auth.backends.ModelBackend",
   # it should be the last entry to prevent unauthorized access
   "guest_user.backends.GuestBackend", #new line
]
```
Add url routing in `urls.py` for the guest and user authentication applications.
```python
urlpatterns = [
   # ... other patterns
   path("accounts/", include("accounts.urls")),
   path("guest/", include("guest_user.urls")),
]
```
Last but not least, prepare the guest user table by running migrations.
```python
python manage.py migrate
```

# Credit
`Guest User` Functionality Has Been Implemented From [This](https://django-guest-user.readthedocs.io/en/latest/index.html) Module  