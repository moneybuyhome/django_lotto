# Generated by Django 3.2 on 2023-07-05 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuessNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('text', models.CharField(max_length=255)),
                ('lottos', models.CharField(default='[1, 2, 3, 4, 5, 6]', max_length=255)),
                ('num_lotto', models.IntegerField(default=5)),
                ('update_date', models.DateTimeField()),
            ],
        ),
    ]
