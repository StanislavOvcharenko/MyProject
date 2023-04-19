# Generated by Django 4.1.7 on 2023-04-13 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_servicestation_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicestation',
            name='company',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
