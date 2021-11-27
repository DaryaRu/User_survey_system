# Generated by Django 3.2.9 on 2021-11-27 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_alter_question_question_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnonymousUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'anonymous_users',
            },
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='survey.anonymoususer'),
        ),
        migrations.AlterField(
            model_name='usersurvey',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_surveys', to='survey.anonymoususer'),
        ),
    ]