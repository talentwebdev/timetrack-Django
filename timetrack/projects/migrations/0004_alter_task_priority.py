# Generated by Django 3.2.8 on 2021-10-07 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20211007_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(blank=True, choices=[('LOW', 'low'), ('MEDIUM', 'medium'), ('HIGH', 'high')], default=None, help_text='Priority choices', max_length=10, null=True),
        ),
    ]
