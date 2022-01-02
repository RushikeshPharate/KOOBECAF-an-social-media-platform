# Generated by Django 3.2.7 on 2021-12-02 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('pages', '0005_followers_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='followers',
            name='user_email',
        ),
        migrations.AlterField(
            model_name='followers',
            name='user_id',
            field=models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
    ]