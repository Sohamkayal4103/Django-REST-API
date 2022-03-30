# Generated by Django 4.0.3 on 2022-03-29 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('ProjectId', models.AutoField(primary_key=True, serialize=False)),
                ('ProjectName', models.CharField(max_length=500)),
                ('ProjectDepartment', models.CharField(max_length=500)),
                ('ProjectDivision', models.CharField(max_length=500)),
                ('ProjectDomain', models.CharField(max_length=500)),
                ('ProjectDescription', models.CharField(max_length=500)),
                ('ProjecTechStacks', models.CharField(max_length=500)),
                ('ProjectDuration', models.CharField(max_length=500)),
                ('ProjectMentor', models.CharField(max_length=500)),
                ('ProjectCode', models.CharField(max_length=500)),
                ('ProjectTeam', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=500)),
                ('UserDepartment', models.CharField(max_length=500)),
                ('UserDivision', models.CharField(max_length=500)),
                ('UserEmail', models.CharField(max_length=500)),
                ('UserRole', models.CharField(max_length=500)),
            ],
        ),
    ]
