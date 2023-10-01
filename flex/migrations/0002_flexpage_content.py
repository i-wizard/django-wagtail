# Generated by Django 4.2.5 on 2023-10-01 12:43

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexpage',
            name='content',
            field=wagtail.fields.StreamField([('tite_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.blocks.TextBlock(help_text='Add additional text', required=True))]))], blank=True, null=True, use_json_field=True),
        ),
    ]