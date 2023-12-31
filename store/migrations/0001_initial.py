# Generated by Django 3.1.1 on 2023-06-15 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_latitude', models.FloatField()),
                ('destination_longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=200)),
                ('hospital_address', models.CharField(max_length=200)),
                ('latitude', models.CharField(max_length=200)),
                ('longitude', models.CharField(max_length=200)),
                ('phone_number', models.CharField(default='no phone number', max_length=200)),
                ('placepageUri', models.CharField(default='no place page uri', max_length=200)),
                ('email', models.EmailField(default='hospital@gmail.com', max_length=254)),
                ('website', models.URLField(default='https://www.google.com/')),
                ('services_offered', models.CharField(default='Support Services, Diagnostic Services,Maternity Services,  Pediatric Services', max_length=50000, null=True)),
                ('ambulance_available', models.BooleanField(default=False)),
                ('ambulance_contacts', models.CharField(default='07082942385', max_length=50000)),
                ('vacancies_available', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, default="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries", max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='photos/products')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('pricing', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(choices=[('ambulance', 'Ambulance'), ('medical_shuttle', 'Medical Shuttle')], max_length=20)),
                ('vehicle_name', models.CharField(max_length=50)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('contact', models.CharField(max_length=200)),
                ('availability', models.BooleanField(default=True)),
                ('price_per_km', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProvided',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=100)),
                ('payment_method', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(max_length=100)),
                ('service', models.CharField(max_length=100)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accepted_payment_services', to='store.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('qualification', models.CharField(max_length=200)),
                ('specialty', models.CharField(max_length=200)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='HospitalService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pricing', models.CharField(max_length=200)),
                ('availability', models.BooleanField(default=False)),
                ('slots', models.IntegerField()),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospital_services', to='store.hospital')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.service')),
            ],
        ),
        migrations.AddField(
            model_name='hospital',
            name='accepted_paymentservices',
            field=models.ManyToManyField(related_name='hospitals', to='store.PaymentService'),
        ),
        migrations.AddField(
            model_name='hospital',
            name='hospital_appointments',
            field=models.ManyToManyField(related_name='hospitals', to='store.Appointment'),
        ),
        migrations.AddField(
            model_name='hospital',
            name='service_provided',
            field=models.ManyToManyField(related_name='hospitals', to='store.ServiceProvided'),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specialty', models.CharField(max_length=100)),
                ('available_from', models.DateField()),
                ('available_to', models.DateField()),
                ('contact_number', models.CharField(max_length=20)),
                ('hospitals_worked', models.ManyToManyField(related_name='doctors', to='store.Hospital')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='store.hospital'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.service'),
        ),
    ]
