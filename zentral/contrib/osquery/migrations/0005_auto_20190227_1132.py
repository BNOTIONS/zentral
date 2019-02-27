# Generated by Django 2.1.7 on 2019-02-27 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('osquery', '0004_auto_20180529_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='configuration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='osquery.Configuration'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='distributor_content_type',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='contenttypes.ContentType'),
        ),
    ]