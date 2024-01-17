# Generated by Django 4.2.7 on 2023-11-28 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_task_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['user', 'deadline', 'priority']},
        ),
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], default=2),
        ),
        migrations.AlterOrderWithRespectTo(
            name='task',
            order_with_respect_to=None,
        ),
    ]
