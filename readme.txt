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
                >django-admin.py version
7.django help 
                > django-admin help
8.StartProject  (Main Application)
                > django-admin.py startproject chiku .  // . means current Directory

### Another Stylre to Create and run Django project :
                > pipenv install django == 2.2
                > pipenv shell
                > django-admin startproject chiku .
                
                
9. Install Linter on VScode for virtual Environment that handle some issues maybe occur.
                VScode -> shift+CMD+p -> interpreter -> python 3.7.1 ('venv':venv)

10.Git Version Control 
                > git init 
                create .gitignore file in root of project  (use www.gitignore.io) -> django
                Push to my local Repository :
                > git add. && git commit -m 'initial commit'




