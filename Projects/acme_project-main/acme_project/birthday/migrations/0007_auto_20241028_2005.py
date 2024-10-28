# Generated by Django 3.2.16 on 2024-10-28 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0006_alter_congratulations_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20, verbose_name='Тег')),
            ],
        ),
        migrations.AddField(
            model_name='birthday',
            name='tags',
            field=models.ManyToManyField(blank=True, help_text='Удерживайте Ctrl для выбора нескольких вариантов', to='birthday.Tag', verbose_name='Теги'),
        ),
    ]
