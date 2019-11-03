# Generated by Django 2.0.3 on 2019-11-03 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraItemCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toppingCost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ExtraSelected',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PizzaCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizzaCost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PizzaNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=100)),
                ('pizzaName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availableSizeOfPizza', to='orders.PizzaNames')),
            ],
        ),
        migrations.CreateModel(
            name='PizzaSizeSelected',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizzaName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selectedSizeOfPizza', to='orders.PizzaNames')),
                ('selectedPizzaSize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.PizzaSize')),
            ],
        ),
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toppingName', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='pizzacost',
            name='pizzaName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myPizzaCost', to='orders.PizzaNames'),
        ),
        migrations.AddField(
            model_name='pizzacost',
            name='pizzaSize',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myPizzaSize', to='orders.PizzaSize'),
        ),
        migrations.AddField(
            model_name='extraselected',
            name='pizzaName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myPizzaExtraSelected', to='orders.PizzaNames'),
        ),
        migrations.AddField(
            model_name='extraselected',
            name='toppingsSelected',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myToppingSelected', to='orders.Toppings'),
        ),
        migrations.AddField(
            model_name='extraitemcost',
            name='toppingName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myTopping', to='orders.Toppings'),
        ),
    ]
