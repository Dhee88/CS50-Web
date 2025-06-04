📘 CS50 Web Programming – Week 0 Notes (Git, GitHub, Django Basics)

1. Version Control with Git
- Git tracks changes in code; GitHub hosts repositories online.
- Synchronizes code between different people
- Test changes to code without losing the original
- Revert back to old versions of code
- Common Git Commands:
  - git init – Initialize a repo
  - git status – Show current changes
  - touch nameoffile.html – Creates a new html file  
  - git add <file> – Stage changes
  - git commit -m "message" – Commit with a message
  - git log – View commit history
  - git clone <url> – Clone a repo
  - git push – Push to remote(To github)
  - git pull – Pull from remote
  - git reset – To go to previous state of repository
      - git reset --hard <commit>
      - git reset --hard origin/master
- Workflow:
  git init → edit → git add . → git commit -m "msg" → git push

- Merge Conflicts 
  - When there is changes made on the same part of the code by different people

- Branching
  - To work on different parts of the repositiory simultaneously
  - Branching commands
    - git branch – Shows the current branch you're on and what branches exist
    - git checkout -b <branch> – To create and switch to a new branch
    - git checkout <branch> – To switch to an already existing branch
    - git merge <branch> –  To merge the branch with the current branch you're on

2. GitHub
- Remote repo hosting with collaboration tools.
- Set remote: git remote add origin <url>
- First push: git push -u origin main
- Fork: To copy someone else's code to edit and update
- Github pages

3. Django Introduction
- Django: Python web framework for rapid development.
- Create project: django-admin startproject myproject
- Run server: python manage.py runserver
- Create app: python manage.py startapp myapp

4. Django Project Structure
- manage.py – CLI for project commands
- project/ – Contains settings.py, urls.py
- app/ – Contains views.py, models.py, etc.
- Add app in settings.py → INSTALLED_APPS

5. Views and URLs
- views.py example:
    from django.http import HttpResponse
    def index(request):
        return HttpResponse("Hello, world!")
- urls.py example:
    from django.urls import path
    from . import views
    urlpatterns = [
        path("", views.index, name="index")
    ]

6. Templates
- HTML files stored in templates/ folder
- Django Template Language: 
    {{ variable }} for dynamic content
    {% for item in list %} ... {% endfor %}
- Render template:
    from django.shortcuts import render
    return render(request, "template.html", context)

7. Static Files
- Stored in static/ directory
- Use {% load static %} and {% static "file.css" %}
- Configure STATIC_URL in settings.py

8. Template Inheritance
- IF there is a common layout 
- Create a html file to store the common layout
- {% extends "tasks/layout.html" %}
- {% block body %} and {% endblock %}

- {% url 'index' %}
- {% url 'task: index' %}
- method='post' in <forms>
- {% csrf_token %}
- if request.method== "POST":
- form = NewTask(request.POST)
- if form.is_valid()
      form.cleaned_data
- return HttpResponseRedirect(reverse("tasks:index"))
- if "tasks" not in request.session
    request.session["tasks"] = []
-{% for loop %}
 {% empty % }
   No tasks
 {% endfor %}

9. Admin & Migrations
- Create admin: python manage.py createsuperuser
- DB changes: 
    - python manage.py makemigrations
    - python manage.py migrate

10. Useful Django Commands
- django-admin startproject projectname
- python manage.py startapp appname
- python manage.py runserver
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py shell
- python manage.py collectstatic

