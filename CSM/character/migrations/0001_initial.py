# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 02:00
from __future__ import unicode_literals

import character.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('spells', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accessed', models.DateTimeField(auto_now=True)),
                ('char_name', models.CharField(blank=True, max_length=1024, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('portrait', models.ImageField(blank=True, null=True, upload_to='')),
                ('char_age', models.SmallIntegerField(blank=True, null=True)),
                ('char_height', models.SmallIntegerField(blank=True, null=True)),
                ('char_weight', models.SmallIntegerField(blank=True, null=True)),
                ('char_skin_color', models.CharField(blank=True, max_length=128, null=True)),
                ('char_hair_color', models.CharField(blank=True, max_length=128, null=True)),
                ('char_eye_color', models.CharField(blank=True, max_length=128, null=True)),
                ('personality', models.TextField(blank=True, null=True)),
                ('ideals', models.TextField(blank=True, null=True)),
                ('bonds', models.TextField(blank=True, null=True)),
                ('flaws', models.TextField(blank=True, null=True)),
                ('allies', models.CharField(blank=True, max_length=512, null=True)),
                ('organizations', models.CharField(blank=True, max_length=512, null=True)),
                ('char_xp', models.IntegerField(blank=True, default=0, null=True)),
                ('STR_score', character.models.IntegerMinMaxField(blank=True, max_value=20, min_value=1, null=True)),
                ('DEX_score', character.models.IntegerMinMaxField(blank=True, max_value=20, min_value=1, null=True)),
                ('CON_score', character.models.IntegerMinMaxField(blank=True, max_value=20, min_value=1, null=True)),
                ('INT_score', character.models.IntegerMinMaxField(blank=True, max_value=20, min_value=1, null=True)),
                ('WIS_score', character.models.IntegerMinMaxField(blank=True, max_value=20, min_value=1, null=True)),
                ('CHA_score', character.models.IntegerMinMaxField(blank=True, max_value=20, min_value=1, null=True)),
                ('STR_saving_throw', models.BooleanField(default=False)),
                ('DEX_saving_throw', models.BooleanField(default=False)),
                ('CON_saving_throw', models.BooleanField(default=False)),
                ('INT_saving_throw', models.BooleanField(default=False)),
                ('WIS_saving_throw', models.BooleanField(default=False)),
                ('CHA_saving_throw', models.BooleanField(default=False)),
                ('death_fails', models.SmallIntegerField(default=0)),
                ('death_successes', models.SmallIntegerField(default=0)),
                ('max_health', models.SmallIntegerField(default=0)),
                ('current_health', models.SmallIntegerField(default=0)),
                ('temp_addtl_hp', models.SmallIntegerField(default=0)),
                ('speed', models.SmallIntegerField(default=30)),
                ('inspiration', models.SmallIntegerField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='ClassLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_level', character.models.IntegerMinMaxField(max_value=20, min_value=1)),
            ],
        ),
        migrations.CreateModel(
            name='SpellsReady',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spell_ready', models.BooleanField(default=False)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spellsready', to='character.Character')),
                ('spells', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spellsready', to='spells.Spell')),
            ],
            options={
                'verbose_name': 'Spell Ready',
                'verbose_name_plural': 'Spells Ready',
            },
        ),
    ]
