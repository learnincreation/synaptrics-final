# Generated by Django 3.1 on 2020-10-15 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('report', '0016_auto_20201015_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailydrcallreport',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='DailyDrMeetingReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dr_speciality', models.CharField(choices=[('NEUROLOGIST', 'NEUROLOGIST'), ('NEUROSURGEON', 'NEUROSURGEON'), ('PSYCHIATRIST', 'PSYCHIATRIST'), ('PHYSICIAN', 'PHYSICIAN'), ('GENRAL PHYSICIAN', 'GENRAL PHYSICIAN'), ('GYNAECOLOGIST', 'GYNAECOLOGIST'), ('SURGEON', 'SURGEON'), ('ORTHOLOGIST', 'ORTHOLOGIST')], max_length=100)),
                ('meeting_place', models.CharField(choices=[('DR CLINIC', 'DR CLINIC'), ('HOSPITAL', 'HOSPITAL'), ('RESIDENCE HOME ADDRESS', 'RESIDENCE HOME ADDRESS')], max_length=100)),
                ('Date_time', models.DateTimeField(auto_now=True)),
                ('dr_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.drmasterlist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
    ]
