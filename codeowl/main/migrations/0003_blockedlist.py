# Generated by Django 4.0.1 on 2022-01-21 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_userupgrade_email_confirmed'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockedList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ips', models.TextField()),
            ],
            options={
                'verbose_name': 'Список заблокированных IP-адресов',
                'verbose_name_plural': 'Списки заблокированных IP-адресов',
            },
        ),
    ]
