# Generated by Django 2.1.5 on 2019-03-01 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=9)),
                ('title', models.CharField(max_length=100)),
                ('student1_name', models.CharField(max_length=50)),
                ('student2_name', models.CharField(blank=True, max_length=50, null=True)),
                ('student3_name', models.CharField(blank=True, max_length=50, null=True)),
                ('student4_name', models.CharField(blank=True, max_length=50, null=True)),
                ('student5_name', models.CharField(blank=True, max_length=50, null=True)),
                ('student1_no', models.IntegerField()),
                ('student2_no', models.IntegerField(blank=True, null=True)),
                ('student3_no', models.IntegerField(blank=True, null=True)),
                ('student4_no', models.IntegerField(blank=True, null=True)),
                ('student5_no', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(max_length=1000)),
                ('mentor', models.CharField(max_length=100)),
                ('domain', models.CharField(max_length=100)),
                ('tools_used', models.CharField(blank=True, max_length=100, null=True)),
                ('report_link', models.CharField(blank=True, max_length=100, null=True)),
                ('awards', models.CharField(blank=True, max_length=100, null=True)),
                ('programme', models.CharField(choices=[('UG', 'UnderGraduate'), ('PG', 'PostGraduate')], max_length=2)),
                ('type', models.CharField(choices=[('IN', 'Internal'), ('EX', 'External')], max_length=2)),
                ('scope', models.CharField(max_length=1000)),
            ],
        ),
    ]
