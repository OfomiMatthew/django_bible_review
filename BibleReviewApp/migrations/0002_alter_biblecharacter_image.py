# Generated by Django 4.1.5 on 2023-01-14 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BibleReviewApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biblecharacter',
            name='image',
            field=models.ImageField(upload_to='BibleReviewApp/images/'),
        ),
    ]
