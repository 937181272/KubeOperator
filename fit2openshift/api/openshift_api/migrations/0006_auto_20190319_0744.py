# Generated by Django 2.1.2 on 2019-03-19 07:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('openshift_api', '0005_volume'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostInfo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('memory', models.BigIntegerField(default=0)),
                ('os', models.CharField(default='', max_length=128)),
                ('os_version', models.CharField(default='', max_length=128)),
                ('cpu_core', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='host',
            name='cpu_core',
        ),
        migrations.RemoveField(
            model_name='host',
            name='memory',
        ),
        migrations.RemoveField(
            model_name='host',
            name='os',
        ),
        migrations.RemoveField(
            model_name='host',
            name='os_version',
        ),
        migrations.AddField(
            model_name='host',
            name='host_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='host_info', to='openshift_api.HostInfo'),
        ),
    ]
