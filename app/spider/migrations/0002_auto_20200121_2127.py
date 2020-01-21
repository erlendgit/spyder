# Generated by Django 3.0.2 on 2020-01-21 20:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('spider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedcategory',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'Feed category',
                'verbose_name_plural': 'Feed categories',
            },
        ),
        migrations.AddField(
            model_name='newsfeed',
            name='slug',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='newsfeed',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='category', to='spider.Feedcategory'),
        ),
    ]