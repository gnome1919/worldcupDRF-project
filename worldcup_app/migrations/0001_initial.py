# Generated by Django 4.0.4 on 2022-07-02 07:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Confederation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_group', models.CharField(blank=True, max_length=1, verbose_name='Group')),
                ('match_date', models.DateField(verbose_name='Date')),
                ('match_time', models.TimeField(verbose_name='Time')),
                ('home_goals', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='Home Goals')),
                ('away_goals', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='Away Goals')),
            ],
            options={
                'verbose_name_plural': 'Matches',
            },
        ),
        migrations.CreateModel(
            name='UserPrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_goals', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='Home Goals')),
                ('away_goals', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='Away Goals')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_edited', models.DateTimeField(auto_now=True, verbose_name='Date Edited')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_predictions_matches', to='worldcup_app.match')),
                ('user_prediction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_predictions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(2006)], verbose_name='Year')),
                ('confederation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldcup_app.confederation')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('confederation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldcup_app.confederation')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_teams_matches', to='worldcup_app.team'),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_teams_matches', to='worldcup_app.team'),
        ),
        migrations.AddField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tournament_matches', to='worldcup_app.tournament'),
        ),
    ]
