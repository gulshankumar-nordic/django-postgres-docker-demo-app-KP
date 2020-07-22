# Generated by Django 3.0.7 on 2020-07-22 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leagueapp', '0004_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='height',
            field=models.FloatField(default=None, help_text='In cms', max_length=25),
        ),
        migrations.AlterField(
            model_name='player',
            name='weight',
            field=models.FloatField(default=None, help_text='In kgs', max_length=25),
        ),
        migrations.CreateModel(
            name='PlayerInTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagueapp.Player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagueapp.Team')),
            ],
        ),
    ]
