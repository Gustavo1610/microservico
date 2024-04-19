# Generated by Django 5.0.4 on 2024-04-19 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MicroServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=8)),
                ('produto', models.CharField(max_length=20)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
