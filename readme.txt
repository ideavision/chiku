1.Make Project Directory 
                > mkdit chiku
2.Create venv 
                > python3 -m venv ./venv
3.Activate venv 
                > . venv/bin/activate
4.Create readme.txt (Useful informations of project) & requirement.txt (Packages that needs in to the project)
                > touch readme.txt requirements.txt
5.Check and Write packages in requirements.txt 
                > pip3 freeze > requirements.txt
6.Install django 
                > pip3 install django
                > django-admin.py version
7.django help 
                > django-admin help
8.StartProject  (Main Application)
                > django-admin.py startproject chiku .  // . means current Directory

### Another Stylre to Create and run Django project :
                > pipenv install django == 2.2
                > pipenv shell
                > django-admin startproject chiku .
                
                
9.Install Linter on VScode for virtual Environment that handle some issues maybe occur.
                VScode -> shift+CMD+p -> interpreter -> python 3.7.1 ('venv':venv)

10.GIT Version Control 
                > git init 
                create .gitignore file in root of project  (use www.gitignore.io) -> django
                Push to my local Repository :
                > git add. && git commit -m 'initial commit'

11. RUN SERVER
                > python3 manage.py runserver

12.PROJECT DESCRIPTION:
    chiku -> setting.py
        > BASE_DIR , SECRET_KEY , DEBUG , ALLOW_HOSTS , INSTALLED_APPS , MIDDLE_WARE , ROOT_URLCONF , TEMPLATES , WSGI_APPLICATION , DATABASES , AUTH_PASSWORD_VALIDATION
    chiku -> urls.py
    chiku -> wsgi.py

13.Creating The Pages App 
        > python3 manage.py startapp pages
        migrations, __init__.py , admin.py , apps.py, models.py , tests.py, views.py

14.Setting pages app

    -> chiku -> etting.py -> INSTALLED_APP=[pages.apps.PagesConfig .]
    -> chiku -> chiku -> apps.py -> class PagesConfig(AppConfig):
                                            name='page'
    -> Create pages app urls : chiku -> chiku -> pages-> urls.py
    from django.urls import path
    from . import views 
    urlpatterns= [
            path('',views.index,name='index')
    ]

15.Create index method in to views.py (Controller)    
        chiku -> pages -> views.py
        from django.shortcuts import render
        from dango.http import HttpResponse
        def index(request):
            return HttpResponse ('<h1>INDEx method from Pages appp</h1>')

16.Setting manin urls.py for pages app
        chiku -> chiku -> urls.py
        from django.urls import path, include 
        urlpatterns=[
        path('',include('pages.urls'))
        ]

17.pages Templates & Based Layout
Create Folder chiku -> templates -> pages (index.html , about.html)
              chiku -> setting.py
                    TEMPLATES=[os.path.join(BASE_DIR,'templates')]
              chiku -> pages ->urls.py
                    urlpatterns=[
                        path('about', views.about, name='about')
                    ]
              chiku -> pages -> views.py
                    create a file in template base.html
                    <html>
                        <body>
                        ##### USE JINJA Template engine for django #####
                        {% block content %}

                        {% endblock %}
                        ##### USE JINJA Template engine for django #####

                        in index.html or about.html 
                        {% extends 'base.html' %}
                        {% block content%}
                            <h1>Home Template use JINJA</h1>
                        {% endblock %}


        add index.html (with jinja syntax), about.html(with jinja syntax) in templates/pages & add base.html in /template/
        edit chiku-> pages -> views.py
                        def index(request):
                        return render(request, 'pages/index.html') 

                        def about(request):
                        return render(request, 'pages/about.html')
                        

18. Install VScode jinja Extension

19.Setting STATIC file & Paths
    create a folder called static includes css/javascript/webfonts/img
    chiku -> setting.py 
            STATIC_ROOT=os.path.join(BASE_DIR,'static')
            STATIC_URL='/static'
            STATICFILES_DIR=[
            os.path.join(BASE_DIR,'chiku/static')
            ]

            check manage.py help 
                > python3 manage.py help

    > python3 manage.py collectstatic

    add main static into .gitignore

20.Bootstrap Layout Configuration
    copy and past all bootstrap css,js, file in base.html
     
    -> base.html
    {% load static %}
    // CSS 
    <link rel="stylesheet" href="{% static 'css/all.css' %}">
    <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}">
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    <link rel="stylesheet" href="{% static 'css/lightbox.min.css'%}">

    //JS
    <script src="{% static 'js/jquery-3.3.1.min.js' %}"></script>
    <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
    <script src="{% static 'js/main.js' %}"></script>


    Config bootstrap Navbar
    Create Templates -> partials create _navbar.html, _topbar.html, _footer.html
    add each part in to the related html files from bootstrap template
    open base.html and add following jinja template code 
    {% include 'partials/_topbar.html' %}
    {% include 'partials/-navbar.html' %}
    {% block content %} {% endblock %} // refer to template/index.html
    {% include 'partial/_footer.html' %}
    also logo
    {% load static %}
    <img src="{% static 'img/logo.png' %}">

    





                         






                        

