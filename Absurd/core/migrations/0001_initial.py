# Generated by Django 2.2.4 on 2020-12-04 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Prompt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prompts', to='core.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('promptNext', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='befores', to='core.Prompt')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='core.Tag')),
            ],
        ),
    ]