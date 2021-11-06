## DJANGO KIDSACADEMY
Building Kidsacademy Application Using Django Version 3.2


### 1. Initial Setup

        .gitignore
        README.md


### 2. Create and push repository to Github

* [Github repo](https://github.com/gurnitha/django-kidsacademy)


### 3. Create django project 'config'

        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


### 4. Create django app 'apps/home' and register to the project

        modified:   README.md
        new file:   apps/home/__init__.py
        new file:   apps/home/admin.py
        new file:   apps/home/apps.py
        new file:   apps/home/migrations/__init__.py
        new file:   apps/home/models.py
        new file:   apps/home/tests.py
        new file:   apps/home/views.py
        modified:   config/settings.py


### 4. HOME PAGE - Create home page - TVUrls

        modified:   README.md
        new file:   apps/home/templates/home/index.html
        new file:   apps/home/urls.py
        modified:   apps/home/views.py
        modified:   config/urls.py


### 4.1 HOME PAGE - Adding and load static files

        modified:   README.md
        modified:   apps/home/templates/home/index.html
        modified:   config/settings.py
        ..
        new file:   static/assets/js/velocity.min.js


### 4.2 HOME PAGE - Create base template

        modified:   README.md
        modified:   apps/home/templates/home/index.html
        modified:   config/settings.py
        new file:   templates/base.html


### 4.3 HOME PAGE - Template inheritance (base template)

        modified:   README.md
        modified:   templates/base.html
        new file:   templates/inc/footer.html
        new file:   templates/inc/head.html
        new file:   templates/inc/header.html
        new file:   templates/inc/mobile_menu.html
        new file:   templates/inc/scripts.html
        new file:   templates/inc/subscribe.html



































































































































































































