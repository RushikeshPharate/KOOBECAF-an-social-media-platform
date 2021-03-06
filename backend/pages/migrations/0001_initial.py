# Generated by Django 3.2.7 on 2021-11-17 20:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('pageName', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('pageEmail', models.EmailField(max_length=254)),
                ('pageDecription', models.TextField(max_length=200)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('followersCount', models.IntegerField()),
                ('pageAuthor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('pageName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.pages')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]
