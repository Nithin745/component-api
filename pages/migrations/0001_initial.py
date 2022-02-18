# Generated by Django 4.0.2 on 2022-02-18 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_content', models.TextField(max_length=0, null=True)),
                ('sub_content', models.TextField(max_length=0, null=True)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_type', to='pages.type')),
            ],
        ),
    ]
