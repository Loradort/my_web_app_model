# Generated by Django 4.2.2 on 2023-07-27 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapge', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='prefix_chioces',
            field=models.IntegerField(choices=[(1, 'นาย'), (2, 'นางสาว'), (3, 'นาง')], default=1),
        ),
    ]
