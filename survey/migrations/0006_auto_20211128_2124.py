# Generated by Django 3.2.9 on 2021-11-28 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_rename_question_usersurvey_survey'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='selected_options',
            field=models.ManyToManyField(to='survey.Option'),
        ),
        migrations.DeleteModel(
            name='AnswerOption',
        ),
    ]
