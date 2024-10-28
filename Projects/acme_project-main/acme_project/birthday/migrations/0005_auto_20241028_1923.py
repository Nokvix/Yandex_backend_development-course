# Generated by Django 3.2.16 on 2024-10-28 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('birthday', '0004_congratulations'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='congratulations',
            options={'ordering': ('created_at',)},
        ),
        migrations.AddField(
            model_name='congratulations',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='congratulations',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]