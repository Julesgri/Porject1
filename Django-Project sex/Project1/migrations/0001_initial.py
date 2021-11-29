# Generated by Django 3.2.9 on 2021-11-27 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Position_name', models.CharField(max_length=200)),
                ('Description', models.TextField(null=True)),
                ('img', models.URLField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.IntegerField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project1.position')),
            ],
        ),
    ]
