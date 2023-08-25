# Generated by Django 4.2.4 on 2023-08-25 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="conditions",
            field=models.ManyToManyField(
                blank=True,
                related_name="products",
                to="product.condition",
                verbose_name="Conditions",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="features",
            field=models.ManyToManyField(
                blank=True,
                related_name="products",
                to="product.feature",
                verbose_name="Features",
            ),
        ),
    ]
