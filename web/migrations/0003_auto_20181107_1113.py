# Generated by Django 2.1 on 2018-11-07 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0002_auto_20181107_0617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('MR', 'MR'), ('MISS', 'Miss'), ('MRS', 'Mrs')], default='MR', max_length=4)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('county', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('postcode', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('mobilephone', models.CharField(blank=True, max_length=10)),
                ('fax', models.CharField(blank=True, max_length=10)),
                ('workphone', models.CharField(blank=True, max_length=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Member')),
            ],
        ),
        migrations.AlterField(
            model_name='pictures',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
