# Generated by Django 5.1.6 on 2025-03-07 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0003_changepatient_policyverification'),
    ]

    operations = [
        migrations.CreateModel(
            name='CFormDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=10)),
                ('uhid', models.CharField(max_length=50, unique=True)),
                ('ip_no', models.CharField(blank=True, max_length=50, null=True)),
                ('adm_dr', models.CharField(max_length=50)),
                ('ward', models.CharField(max_length=50)),
                ('patient_type', models.CharField(choices=[('OPD', 'OPD'), ('IPD', 'IPD')], max_length=3)),
                ('tarrif_name', models.CharField(max_length=50)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('advance_serach_option', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentTransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=10)),
                ('uhid', models.CharField(max_length=50, unique=True)),
                ('ip_no', models.CharField(blank=True, max_length=50, null=True)),
                ('adm_dr', models.CharField(max_length=50)),
                ('ward', models.CharField(max_length=50)),
                ('patient_type', models.CharField(choices=[('OPD', 'OPD'), ('IPD', 'IPD')], max_length=3)),
                ('tarrif_name', models.CharField(max_length=50)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('advance_serach_option', models.TextField()),
            ],
        ),
    ]
