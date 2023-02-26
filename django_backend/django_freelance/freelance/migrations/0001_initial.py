# Generated by Django 4.1.7 on 2023-02-26 14:17

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
                ('phone', models.CharField(max_length=11)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Executor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('desc', models.CharField(max_length=1000)),
                ('price', models.IntegerField()),
                ('order_type', models.CharField(choices=[('1', 'Веб разработка'), ('2', 'Маркетинг'), ('3', 'Копирайтинг'), ('4', 'Рерайтинг'), ('5', 'Переводы'), ('6', 'Видеомонтаж'), ('7', 'Фотография')], default='1', max_length=1)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelance.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], default='1', max_length=1)),
                ('desc', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('desc', models.CharField(max_length=1000)),
                ('price', models.IntegerField()),
                ('service_type', models.CharField(choices=[('1', 'Веб разработка'), ('2', 'Маркетинг'), ('3', 'Копирайтинг'), ('4', 'Рерайтинг'), ('5', 'Переводы'), ('6', 'Видеомонтаж'), ('7', 'Фотография')], default='1', max_length=1)),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelance.executor')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('severity', models.CharField(choices=[('1', 'Низкая'), ('2', 'Средняя'), ('3', 'Высокая')], default='1', max_length=1)),
                ('desc', models.CharField(max_length=1000)),
                ('ticket_date', models.DateTimeField()),
                ('is_resolved', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='freelance.customer')),
                ('executor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='freelance.executor')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='freelance.order')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='freelance.service')),
            ],
        ),
        migrations.CreateModel(
            name='Ordering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField()),
                ('deadline', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelance.customer')),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelance.executor')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='freelance.order')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='freelance.service')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_date', models.DateTimeField()),
                ('is_edited', models.BooleanField(default=False)),
                ('desc', models.CharField(max_length=1000)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelance.customer')),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelance.executor')),
            ],
        ),
        migrations.CreateModel(
            name='Authoring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_date', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='freelance.customer')),
                ('executor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='freelance.executor')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelance.review')),
            ],
        ),
    ]
