from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import BookModel


class BooksListCreate(APIView):  # the APIView will return a Json representation of the view
    def get(self, request):
        books = BookModel.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({"books": serializer.data})

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailBookView(APIView):
    def get(self, request, id):
        book = BookModel.objects.get(pk=id)
        serializer = BookSerializer(book)
        return Response({"book": serializer.data})

    def post(self, request, id):
        book = BookModel.objects.get(pk=id)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self):
        book = BookModel.objects.get(pk=id)
        book.delete()
        return Response(status=status.HTTP_200_OK)
