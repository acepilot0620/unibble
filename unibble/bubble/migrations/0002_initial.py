# Generated by Django 3.2.9 on 2021-11-10 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bubble', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.unibber'),
        ),
        migrations.AddField(
            model_name='bubble',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.unibber'),
        ),
    ]
