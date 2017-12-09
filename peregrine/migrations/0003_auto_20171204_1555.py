# -*- coding: utf-8 -*-
# Generated by Django 1.11.8.dev20171024115706 on 2017-12-04 15:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('peregrine', '0002_auto_20171204_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitepage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, help_text='The categories for the page or post.', to='peregrine.Category'),
        ),
        migrations.AlterField(
            model_name='sitepost',
            name='authors',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, help_text='The authors of the post.', to=settings.AUTH_USER_MODEL),
        ),
    ]