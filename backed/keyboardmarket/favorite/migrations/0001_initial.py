# Generated by Django 3.1.5 on 2022-12-28 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_time', models.DateTimeField(auto_now=True, verbose_name='創建時間')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改時間')),
                ('status', models.IntegerField(verbose_name='狀態')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='商品')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='用戶')),
            ],
            options={
                'db_table': 'favorite',
            },
        ),
    ]
