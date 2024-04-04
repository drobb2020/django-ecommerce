# Generated by Django 4.2.8 on 2024-03-13 14:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("payment", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="shippingaddress",
            old_name="address1",
            new_name="shipping_address1",
        ),
        migrations.RenameField(
            model_name="shippingaddress",
            old_name="address2",
            new_name="shipping_address2",
        ),
        migrations.RenameField(
            model_name="shippingaddress",
            old_name="city",
            new_name="shipping_city",
        ),
        migrations.RenameField(
            model_name="shippingaddress",
            old_name="country",
            new_name="shipping_country",
        ),
        migrations.RenameField(
            model_name="shippingaddress",
            old_name="email",
            new_name="shipping_email",
        ),
        migrations.RenameField(
            model_name="shippingaddress",
            old_name="full_name",
            new_name="shipping_full_name",
        ),
        migrations.RenameField(
            model_name="shippingaddress",
            old_name="postal_code",
            new_name="shipping_postal_code",
        ),
        migrations.RenameField(
            model_name="shippingaddress",
            old_name="state",
            new_name="shipping_state",
        ),
    ]
