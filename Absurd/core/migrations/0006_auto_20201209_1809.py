# Generated by Django 2.2.4 on 2020-12-09 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_choice_random'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='promptNext',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='destination', to='core.Prompt'),
        ),
    ]
