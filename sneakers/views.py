from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BrandSerializers, ProductSerializers

# Create your views here.


class CreateBrand(APIView):
    serializer_class = BrandSerializers

    def post(self, request, format=None):
        serialilzer = BrandSerializers(data=request.data)

        if serialilzer.is_valid():
            serialilzer.save()
            return Response({"status": "success", 'message': "Record Saved!"},
                            status=status.HTTP_201_CREATED)


class CreateProducts(APIView):
    serializer_class = ProductSerializers

    def post(self, request, format=None):
        serialilzer = ProductSerializers(data=request.data)

        if serialilzer.is_valid():
            serialilzer.save()
            return Response({"status": "success", 'message': "Record Saved!"},
                            status=status.HTTP_201_CREATED)



