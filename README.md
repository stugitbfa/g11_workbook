# g11_workbook
g11_workbook
# g11_workbook
g11_workbook

1: Create repo in GitHub for project

2: Clone you reop inside your local system 
(common-project-foledr)> git clone *reop-url*

3: Change dir
(common-project-folder)> cd repo-name
...(common-project-folder)/repo-name>

4: make sure you have instaled pyton in your local system
...(common-project-floder)/repo-name>python --version
Python 3.13.3

5: Create virtual environment for project
...(common-project-floder)/repo-name> python -m venv *Your-env-name*

Activate/Deactivate you virtual env:-

Windows:
...(common-project-floder)/repo-name>  *Your-env-name*\Scripts\activate
(*Your-env-name*)...(common-project-floder)/repo-name>

Linux/Mac:
...(common-project-floder)/repo-name> source  *Your-env-name*\Scripts\activate

6: Now, let's install Django
(*Your-env-name*).../repo-name> pip install django==x.y.z

Now,check django is installed or not in your virtual env
(*Your-env-name*).../repo-name> Python -m django version
5.2.3

OR
(*Your-env-name*).../repo-name>python
Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> django.get_version()
'5.2.3'
>>>exit()

OR
(*Your-env-name*).../repo-name> pip list
Package  Version
-------- -------
asgiref  3.8.1
Django   5.2.3
pip      24.0
sqlparse 0.5.3
tzdata   2025.2

OR

(*Your-env-name*).../repo-name> pip freeze
asgiref==3.8.1
Django==5.2.3
sqlparse==0.5.3
tzdata==2025.2

7: Create requirement.txt in your repo-name
(*Your-env-name*).../repo-name> type nul > requirement.txt -windows
(*Your-env-name*).../repo-name> type nul > requirement.txt -linux&mac

add, installed modules and packages inside your requirement.txt
(*Your-env-name*).../repo-name> pip freeze > requirement.txt

Install or Upgrade your modules from requirement.txt
(*Your-env-name*).../repo-name> type nul > pip install -r requirement.txt

8: Now, Creating django project
(*Your-env-name*).../repo-name> django-admin startproject *project-name* .

9: Create Django apps
(*Your-env-name*).../repo-name> mkdir apps

apps /
    - app1 - create dir first
    - app2 

(*Your-env-name*).../repo-name> python manage.py startapp *app-name* apps\*app-name*

Step 9: Create Django Project
Inside your repo root:
(venv) .../gn_project_name> django-admin startproject project .


Now your structure will be:
gn_project_name/
|
├── project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
|
├── manage.py
├── requirements.txt
└── venv/


✅ Step 10: Create Apps Folder and Django Apps
(venv) .../gn_project_name> mkdir apps


Then for each app:
(venv) .../gn_project_name> python manage.py startapp app_name apps/app_name


For example:
(venv) .../gn_project_name> python manage.py startapp web apps/web


✅ Step 11: Configure App Path
Edit apps/web/apps.py:

from django.apps import AppConfig
class WebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.web'


✅ Step 12: Add App to Installed Apps
Edit project/settings.py:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    # Local apps
    'apps.web',
]


✅ Final Directory Structure (Example)
gn_project_name/
|
├── apps/
│   └── web/
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── views.py
│       └── ...
|
├── project/
│   ├── settings.py
│   └── urls.py
|
├── manage.py
├── requirements.txt
└── venv/


✅ Step 13: setup Templates, Static and Media dir
Template setup:
—-------------
Base-dir /
Apps /
App-name /
Templates / - create template dir
App-name - create appname dir
Index.html
Services.html
Blogs.html
about.html
contactus.html


Static & Media setup:
—-------------------
Base-dir /
Apps /
App-name /
Static
Css
Style.css
navbar.css
JS
index.js
Iamges
Fonts


How to access Static/Media files:
—-------------------------
-project/settings.py

Import os
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


-Now, setup Static & Media file urls in project/urls.py

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.crud.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

{% load static %}
<img src="{% static 'my_app/example.jpg' %}" alt="My image">

✅ Step 14: CRUD
C - Create/Insert - create()
R - Read/Show - get(), filter(), 
U - Update - 
D - Delete - delete()

✅ Step 15: Form setup
[S2] <form action="" method="post" enctype="multipart/form-data">
[S2] {% csrf_token %}

