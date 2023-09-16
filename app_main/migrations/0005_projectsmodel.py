# Generated by Django 4.2.4 on 2023-08-30 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0004_publicationmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=555, null=True, verbose_name='Project Title')),
                ('link_git', models.URLField(blank=True, default='https://www.google.com/', null=True, verbose_name='Github Link')),
                ('link_live', models.URLField(blank=True, default='https://www.google.com/', null=True, verbose_name='Live Link')),
            ],
            options={
                'verbose_name': 'Project & Accomplishment',
                'verbose_name_plural': 'Projects & Accomplishments',
                'ordering': ['-id'],
            },
        ),
    ]
