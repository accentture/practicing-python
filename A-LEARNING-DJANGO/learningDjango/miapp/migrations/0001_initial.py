# Generated by Django 3.1.4 on 2021-01-09 22:48

# these are instructions that use Django for its migrations to create it, and after to create tables
from django.db import migrations, models


#create a migration is important to able to change a structure in database
# a migration ocurrs when a change ocurrs in database
# one migration must be created by every change
#when I will execute a migration at produccion, migrations are executed automatically and ocurrs changes in database automatically
# when I work in team and I upload my code to a repository, my classmates will execute my migrations, it allows to have the same verion of database between all members of project
# migration is a way to version of database and doesn't only of code
class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('public', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('created_at', models.DateField()),
            ],
        ),
    ]