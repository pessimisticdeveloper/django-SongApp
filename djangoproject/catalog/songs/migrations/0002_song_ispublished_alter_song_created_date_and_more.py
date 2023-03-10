# Generated by Django 4.1.5 on 2023-01-07 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='isPublished',
            field=models.BooleanField(default=True, verbose_name='Şarkı Yayındamı'),
        ),
        migrations.AlterField(
            model_name='song',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Eklediği Tarih'),
        ),
        migrations.AlterField(
            model_name='song',
            name='description',
            field=models.TextField(verbose_name='Şarkı Açıklaması'),
        ),
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.CharField(max_length=50, verbose_name='Şarkı Resmi'),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Şarkı İsmi'),
        ),
    ]
