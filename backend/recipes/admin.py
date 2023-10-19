from django.contrib import admin

from recipes.forms import NotAllowEmtyForm
from recipes.models import (Favorite, Ingredient, IngredientRecipes, Recipe,
                            ShoppingCart, Tag)


class IngredientRecipeInline(admin.TabularInline):
    model = IngredientRecipes
    extra = 0
    min_num = 1
    formset = NotAllowEmtyForm


class TagInline(admin.TabularInline):
    model = Recipe.tags.through
    extra = 0
    min_num = 1
    formset = NotAllowEmtyForm


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measurement_unit')
    list_filter = ('name', )


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'pub_date')
    list_filter = ('author', 'name', 'tags')
    exclude = ('tags',)
    inlines = [IngredientRecipeInline, TagInline]


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')
    search_fields = ('name', 'slug',)
