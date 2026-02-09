from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0009_alter_certificate_options_alter_certificate_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="certificate",
            name="title_en",
            field=models.CharField(blank=True, max_length=200, verbose_name="Title (EN)"),
        ),
        migrations.AddField(
            model_name="certificate",
            name="title_es",
            field=models.CharField(blank=True, max_length=200, verbose_name="Title (ES)"),
        ),
        migrations.AddField(
            model_name="certificate",
            name="subtitle_en",
            field=models.CharField(
                blank=True,
                max_length=200,
                verbose_name="Subtitle / Organization (EN)",
            ),
        ),
        migrations.AddField(
            model_name="certificate",
            name="subtitle_es",
            field=models.CharField(
                blank=True,
                max_length=200,
                verbose_name="Subtitle / Organization (ES)",
            ),
        ),
        migrations.AddField(
            model_name="certificate",
            name="description_en",
            field=models.TextField(blank=True, verbose_name="Description (EN)"),
        ),
        migrations.AddField(
            model_name="certificate",
            name="description_es",
            field=models.TextField(blank=True, verbose_name="Description (ES)"),
        ),
    ]
