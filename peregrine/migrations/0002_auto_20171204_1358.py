# -*- coding: utf-8 -*-
# Generated by Django 1.11.8.dev20171024115706 on 2017-12-04 13:58
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields
import wagtail.contrib.table_block.blocks
try:
    import wagtail.core.blocks as wagtail.wagtailcore.blocks
    import wagtail.core.fields as wagtail.wagtailcore.fields
    import wagtail.documents.blocks as wagtail.wagtaildocs.blocks
    import wagtail.embeds.blocks as wagtail.wagtailembeds.blocks
    import wagtail.images.blocks as wagtail.wagtailimages.blocks
except ImportError:
    import wagtail.wagtailcore.blocks
    import wagtail.wagtailcore.fields
    import wagtail.wagtaildocs.blocks
    import wagtail.wagtailembeds.blocks
    import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('peregrine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.AlterField(
            model_name='sitepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.TextBlock(icon='title', template='wagtailcontentstream/blocks/heading.html')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'ol', 'ul'], icon='pilcrow')), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.TextBlock(required=False))))), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock()), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')), ('table', wagtail.contrib.table_block.blocks.TableBlock(icon='table')), ('code', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('http', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], help_text='Coding language', label='Language')), ('code', wagtail.wagtailcore.blocks.TextBlock(label='Code'))), icon='code'))), blank=True),
        ),
        migrations.AddField(
            model_name='sitepage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='peregrine.Category'),
        ),
    ]
