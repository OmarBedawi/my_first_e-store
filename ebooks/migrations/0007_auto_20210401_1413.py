# Generated by Django 3.1.6 on 2021-04-01 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ebooks', '0006_ebook_readers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ebook_readers',
            new_name='Ebook_reader',
        ),
    ]
