# Generated by Django 3.2 on 2023-09-11 14:04

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20230831_2351'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorite',
            options={'ordering': ['user'], 'verbose_name': 'Избранный рецепт', 'verbose_name_plural': 'Избранные рецепты'},
        ),
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['name'], 'verbose_name': 'Ингредиент', 'verbose_name_plural': 'Ингредиенты'},
        ),
        migrations.AlterModelOptions(
            name='ingredientrecipes',
            options={'ordering': ['recipe'], 'verbose_name': 'Ингредиент рецепта', 'verbose_name_plural': 'Ингредиенты рецепта'},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Рецепт', 'verbose_name_plural': 'Рецепты'},
        ),
        migrations.AlterModelOptions(
            name='shoppingcart',
            options={'ordering': ['user'], 'verbose_name': 'Корзина покупок', 'verbose_name_plural': 'Корзина покупок'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name'], 'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
        migrations.AddField(
            model_name='recipe',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата и время публикации рецепта'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(max_length=7, unique=True, validators=[django.core.validators.RegexValidator('^#([a-fA-F0-9]{6})', message='Цвет тега должен быть указан в hex формате')], verbose_name='Цвет Тега'),
        ),
    ]
