from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics, status, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .serializers import UserSerializer, ItemSerializer, ImageSerializer, MultipleImageSerializer, PostSerializer
from .models import User, Item, Image, Post

import io #delete

from rest_framework.parsers import JSONParser #delete
from rest_framework.renderers import JSONRenderer #delete


@api_view(['GET', 'POST'])
def user_list(request):

    if request.method == "GET":
        obj = User.objects.all()
        item = Item.objects.all()
        # print(item)
        serializer = UserSerializer(obj, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['GET', 'PUT', 'DELETE'])
def user_edit(request, name):

    try:
        user = User.objects.get(first_name=name)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --> this handles all the methods POST GET PUT DELETE
class ImageView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    # --> detail=false is not sending ids in the url
    @action(detail=False, methods=["POST"])
    def multiple_upload(self, request, *args, **kwargs):
        serializer = MultipleImageSerializer(data=request.data)
        # itemId = int(request.POST.get('itemId'))
        if serializer.is_valid(raise_exception=True):
            images = serializer.validated_data.get('images')
            itemId = serializer.validated_data.get('itemId')
            getItemInstance = Item.objects.get(pk=itemId[0])

            image_list = []
            for img in images:
                print(img)
                image_list.append(
                    Image(image=img, item_id=getItemInstance)
                )

            if image_list:  # --> if imagelist exists
                Image.objects.bulk_create(image_list)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)


# class ItemView(viewsets.ModelViewSet):
#     queryset = Image.objects.all()
#     serializer_class = ItemSerializer

#     @action(detail=False, methods=['POST'])
#     def item_list(self, request, *args, **kwargs):
#         serializer = ItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()


@api_view(['GET', 'POST'])
def item_list(request):

    if request.method == "GET":
        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            # itemId = serializer.validated_data.get('id', )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def item_edit(request, id, username):

    try:
        item = Item.objects.get(pk=id)
        user = User.objects.filter(username=username).first() # maybe filter is better
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserSerializer(item)
        return Response(serializer.data)
    elif request.method == "PUT":
        # serializer = ItemSerializer(item, data=request.data)
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'DELETE'])
def image_list(request, itemId):
    try:
        image = Image.object.get(item_id=itemId)
        print("we have successfully found these images", image)
    except Image.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        # Will check if need ImageSerializer or MultipleImageSerializer
        serializer = ImageSerializer(image)
        return Response(serializer.data)
    elif request.method == "DELETE":
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == "GET":
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def post_edit(request, postId, itemId, userId):
    try:
        post = Post.objects.get(pk=postId)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PUT', 'DELETE', 'POST'])
# def user_edit(request):
#     password = request.data["password"]
#     email = request.data["email"]
#     print(password, email)
#     try:
#         user = User.objects.get(email=email)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     print(request.data["email"])

#     if request.method == "GET":
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = UserSerializer(user)
#         user_password = serializer.data["password"]
#         user_email = serializer.data["email"]
#         if user_password == password and user_email == email:
#             return Response(True, status=status.HTTP_200_OK)
#         return Response(False, status=status.HTTP_401_UNAUTHORIZED)
#     elif request.method == "PUT":
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def hello(request):
    if request.method == "GET":
        # queryset = User.objects.all()
        # serializer_class = UserSerializer
        return Response("Hello this is a test for fucntion based calls")
