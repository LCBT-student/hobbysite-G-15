<<<<<<< HEAD
<<<<<<< HEAD
# Generated by Django 5.0.3 on 2024-05-04 09:44
=======
# Generated by Django 5.0.2 on 2024-05-05 08:36
>>>>>>> commissions

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
=======
# Generated by Django 4.2.10 on 2024-05-05 09:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
>>>>>>> 13409faed6575bd7f2e46678cae18c8e539cefbe


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
<<<<<<< HEAD
                ('name', models.CharField(max_length=50)),
                ('short_bio', models.TextField()),
=======
                ('name', models.CharField(default='A Random Person', max_length=63)),
                ('email_address', models.EmailField(max_length=254)),
>>>>>>> commissions
=======
                ('display_name', models.CharField(max_length=63)),
                ('email', models.EmailField(max_length=254)),
>>>>>>> 13409faed6575bd7f2e46678cae18c8e539cefbe
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
