# Generated by Django 2.1.2 on 2019-03-19 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openshift_api', '0007_auto_20190319_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostinfo',
            name='volumes',
            field=models.ManyToManyField(null=True, to='openshift_api.Volume'),
        ),
    ]
