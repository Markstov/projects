# Generated by Django 2.2.7 on 2019-12-21 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('komp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='status2',
            field=models.CharField(choices=[('4', '4GB'), ('8', '8GB'), ('16', '16GB'), ('128', '128GB')], default='4', max_length=2, verbose_name='Оперативная память'),
        ),
    ]
