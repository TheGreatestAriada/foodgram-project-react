# Generated by Django 3.2 on 2023-08-31 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20230830_2255'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscribe',
            new_name='Subscription',
        ),
        migrations.RemoveConstraint(
            model_name='subscription',
            name='unique_followers',
        ),
        migrations.AddConstraint(
            model_name='subscription',
            constraint=models.UniqueConstraint(fields=('user', 'author'), name='unique_subscriber'),
        ),
    ]
