from django.db import migrations, models
from django.core.validators import MinValueValidator, MaxValueValidator
class Migration(migrations.Migration):
    dependencies = [
        ('booking_manager', '0005_alter_productbooking_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.PositiveIntegerField(
                validators=[
                    MinValueValidator(1),
                    MaxValueValidator(5),
                ],
            ),
        ),
    ]
