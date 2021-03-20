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

    def book_list(self, request):
        list = Book.objects.all()
        serializer = BookSerializer(list, many=True)
        return Response(serializer.data)

    def retrieve(self, request, id):
        queryset = Book.objects.all()
        task = get_object_or_404(queryset, id=id)
        serializer = BookSerializer(task)
        return Response(serializer.data)

    def create(self, request):
        if request.user.role == "Guest":
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

        book = Book.objects.create(name=request.data.get('name'),
                                   price=request.data.get('price'),
                                   description=request.data.get('description'),
                                   created_at=request.data.get('created_at'),
                                   num_pages=request.data.get('num_pages'),
                                   genre=request.data.get('genre'))
        book.save()
        return Response({}, status=status.HTTP_201_CREATED)

    def update(self, request, id):
        if request.user.role == "Guest":
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
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
        if request.user.role == "Guest":
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        book = Book.objects.get(id=id)
        book.delete()
        return Response({}, status=status.HTTP_200_OK)


class JournalViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def journal_list(self, request):
        list = Journal.objects.all()
        serializer = JournalSerializer(list, many=True)
        return Response(serializer.data)

    def retrieve(self, request, id):
        queryset = Journal.objects.all()
        task = get_object_or_404(queryset, id=id)
        serializer = JournalSerializer(task)
        return Response(serializer.data)

    def create(self, request):
        if request.user.role == "Guest":
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        journal = Journal.objects.create(name=request.data.get('name'),
                                         price=request.data.get('price'),
                                         description=request.data.get('description'),
                                         created_at=request.data.get('created_at'),
                                         type=request.data.get('type'),
                                         publisher=request.data.get('publisher'))
        journal.save()
        return Response({}, status=status.HTTP_201_CREATED)

    def update(self, request, id):
        if request.user.role == "Guest":
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
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
        if request.user.role == "Guest":
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        journal = Journal.objects.get(id=id)
        journal.delete()
        return Response({}, status=status.HTTP_200_OK)
