# Generated by Django 4.1.1 on 2022-10-05 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('comment', models.CharField(max_length=122)),
                ('phonenumber', models.TextField(max_length=122)),
                ('date', models.DateField()),
            ],
        ),
    ]