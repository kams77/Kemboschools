# Generated by Django 3.0.5 on 2020-04-08 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0008_auto_20200403_0223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adresse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('pays', models.CharField(blank=True, max_length=100, null=True)),
                ('commune', models.CharField(blank=True, max_length=100, null=True)),
                ('quartier', models.CharField(blank=True, max_length=100, null=True)),
                ('avennue', models.CharField(blank=True, max_length=200, null=True)),
                ('numero', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='myschoolschool',
            name='adress',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SchoolAdress_set', to='Backend.Adresse'),
        ),
    ]
