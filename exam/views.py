from django.urls import path, include
from .models import Customer, Country
from .serializers import CustomerSerializer, CountrySerializer
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.

@api_view(['GET', 'POST'])
def CountryView(request):
    
    if request.method == 'GET':
        qs = Country.objects.filter()
        serializer = CountrySerializer(qs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def CustomerView(request):

    if request.method == 'GET':
        qs = Customer.objects.filter()
        serializer = CustomerSerializer(qs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def CountryDetailView(request, pk):
    
    qs = get_object_or_404(Country, pk=pk)
    
    if request.method == 'GET':
        serializer = CountrySerializer(qs)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CountrySerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT','DELETE'])
def CustomerDetailView(request, pk):
    
    qs = get_object_or_404(Customer, pk=pk)
    
    if request.method == 'GET':
        serializer = CustomerSerializer(qs)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CustomerSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
