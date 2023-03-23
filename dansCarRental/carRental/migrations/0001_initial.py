# Generated by Django 4.0.3 on 2023-03-16 03:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=4)),
                ('price', models.IntegerField(choices=[(100, 'High'), (75, 'Middle'), (50, 'Low')])),
                ('status', models.CharField(choices=[('AV', 'Available'), ('RENT', 'Rented'), ('DIS', 'Disabled')], default='AV', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('customer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='carRental.customer')),
                ('hours', models.IntegerField(default=0)),
                ('rate', models.DecimalField(decimal_places=2, default=15.0, max_digits=6)),
            ],
            bases=('carRental.customer',),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('confirmation_code', models.CharField(max_length=5)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carRental.customer')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carRental.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='carRental.employee')),
            ],
            options={
                'permissions': [('mange_employees', 'Can manage employees')],
            },
            bases=('carRental.employee',),
        ),
    ]
