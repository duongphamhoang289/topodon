# Generated by Django 4.1.1 on 2022-09-15 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_rename_department_name_department_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='depart_incharge_id',
            new_name='department_id',
        ),
        migrations.AlterField(
            model_name='department',
            name='date_created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='date_resolved',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='date_start',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='solution',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('Not Resolvef', 'Not Resolved'), ('Resolved', 'Resolved')], max_length=200, null=True),
        ),
    ]