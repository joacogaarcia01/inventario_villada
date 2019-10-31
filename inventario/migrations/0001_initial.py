# Generated by Django 2.2.6 on 2019-10-31 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id_lab', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('id_type', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id_item', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('desc', models.CharField(blank=True, max_length=20, null=True)),
                ('entry_date', models.DateField(blank=True, null=True)),
                ('id_lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Lab')),
                ('id_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Type')),
            ],
        ),
    ]
