# Generated by Django 3.1.1 on 2020-10-05 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=20, verbose_name='국가명')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('age', models.IntegerField(verbose_name='나이')),
                ('sex', models.CharField(max_length=6, verbose_name='성별')),
                ('name', models.CharField(max_length=10, verbose_name='이름')),
                ('nation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.country')),
            ],
        ),
    ]
