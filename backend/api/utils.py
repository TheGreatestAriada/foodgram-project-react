from django.shortcuts import get_object_or_404
from django.http import FileResponse
from recipes.models import Recipe
from users.models import Subscription
from rest_framework import status


class CreateDeleteMixin():
    @staticmethod
    def create_object(request, pk, serializer_in, serializer_out, model):
        user = request.user.id
        obj = get_object_or_404(model, id=pk)

        data_recipe = {'user': user, 'recipe': obj.id}
        data_subscribe = {'user': user, 'author': obj.id}

        if model is Recipe:
            serializer = serializer_in(data=data_recipe)
        else:
            serializer = serializer_in(data=data_subscribe)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer_to_response = serializer_out(obj, context={'request': request})
        return serializer_to_response


    @staticmethod
    def delete_object(request, pk, model_object, model_for_delete_object):
        user = request.user

        obj_recipe = get_object_or_404(model_object, id=pk)
        obj_subscription = get_object_or_404(model_object, id=pk)

        if model_for_delete_object is Subscription:
            object = get_object_or_404(
                model_for_delete_object, user=user, author=obj_subscription
            )
        else:
            object = get_object_or_404(
                model_for_delete_object, user=user, recipe=obj_recipe
            )
        object.delete()


def send_message(ingredient_lst):
    shopping_list = ['Список покупок:']
    for ingredient in ingredient_lst:
        shopping_list.append('{} ({}) - {}'.format(*ingredient))

    return FileResponse(
        '\n'.join(shopping_list),
        as_attachment=True,
        filename='shopping_list.txt',
        status=status.HTTP_200_OK,
        content_type='text/plain',
    )
