=====
Project1
=====

Project1 is a project made to give you ideas on different sexual positions that you can try. Each position has their possibility of rating.
Detailed documentation is in the "docs" directory.

Quick start
-----------
preRequisite:
install pip.
download python,
download django, 
download pandas.

1. Add "Project1" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'Project1',
    ]

2. Include the Project1 URLconf in your project urls.py like this::

    path('Project1/', include('Project1.urls')),

3. Run ``python manage.py migrate`` to create the polls models. In powershell in the parent forlder of django.

4. add folder BaseDeDonnées in the same directory as Project1.

4. Start the development server and visit http://127.0.0.1:8000/Project1
   'python manage.py runserver'

