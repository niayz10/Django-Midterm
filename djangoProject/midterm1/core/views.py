from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

# Create your views here.
from authm.models import CustomUser
from core.models import Book, Journal
from core.serializers import BookSerializer, JournalSerializer


class BookViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, id):
        queryset = Book.objects.all()
        task = get_object_or_404(queryset, id=id)
        serializer = BookSerializer(task)
        return Response(serializer.data)

    def create(self, request):
        book = Book.objects.create(name=request.data.get('name'),
                                   price=request.data.get('price'),
                                   description=request.data.get('description'),
                                   created_at=request.data.get('created_at'),
                                   num_pages=request.data.get('num_pages'),
                                   genre=request.data.get('genre'))
        book.save()
        return Response({}, status=status.HTTP_201_CREATED)

    def update(self, request, id):
        book = Book.objects.get(id=id)
        book.name = request.data.get('name')
        book.price = request.data.get('price')
        book.description = request.data.get('description')
        book.created_at = request.data.get('created_at')
        book.num_pages = request.data.get('num_pages')
        book.genre = request.data.get('genre')
        book.save()
        return Response({}, status=status.HTTP_200_OK)

    def destroy(self, request, id):
        book = Book.objects.get(id=id)
        book.delete()
        return Response({}, status=status.HTTP_200_OK)


class JournalViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, id):
        queryset = Journal.objects.all()
        task = get_object_or_404(queryset, id=id)
        serializer = JournalSerializer(task)
        return Response(serializer.data)

    def create(self, request):
        journal = Journal.objects.create(name=request.data.get('name'),
                                         price=request.data.get('price'),
                                         description=request.data.get('description'),
                                         created_at=request.data.get('created_at'),
                                         type=request.data.get('type'),
                                         publisher=request.data.get('publisher'))
        journal.save()
        return Response({}, status=status.HTTP_201_CREATED)

    def update(self, request, id):
        journal = Journal.objects.get(id=id)
        journal.name = request.data.get('name')
        journal.price = request.data.get('price')
        journal.description = description = request.data.get('description')
        journal.created_at = request.data.get('created_at')
        journal.type = request.data.get('type')
        journal.publisher = request.data.get('publisher')
        journal.save()
        return Response({}, status=status.HTTP_200_OK)

    def destroy(self, request, id):
        journal = Journal.objects.get(id=id)
        journal.delete()
        return Response({}, status=status.HTTP_200_OK)
