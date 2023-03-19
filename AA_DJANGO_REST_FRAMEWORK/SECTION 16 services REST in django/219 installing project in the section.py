""" 
    VIRTUAL ENVIRONMENT IN PYTHON
        --when work with a project with python, use an virtual envrionmental 
        --it allows to add other modules as django without risk to damage the main installation of python, besides it allows that our projects doesn't crash
        --after to install an virtual environment all modules is isolated


    --to create virtual environment
        py -m venv agenda

    --to activate envrionment
        matplotENV\Scripts\activate.bat

    --to deactivate virtual environment
        cd matplotENV\Scripts\deactivate.bat

    --to install packages for this project
        py -m pip install -r local.txt

    --create database name with the project is working, it database is in secret.json
    --also I can check in agenda/settings/local.py



    #=============================================================CREATING DATABASE
    --creating database in sql shell
        CREATE DATABASE dbemploy;

    --it is not convenient create a dabase open, therefore I indicate that this database will be used by a user with a specifif permission

    --creating user
        CREATE USER jonathan;

    --setting database that will used
        \c dbemploy;

    --giving permissions to user
        ALTER ROLE jonathan WITH PASSWORD 'passwordOfSuperUser';

    --creating database for this project
        create database diarydb



 """