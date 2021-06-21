from django.shortcuts import render

from .models import Profile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProfilePage

@api_view(['POST'])
def loginpage(request):
    serializer = ProfilePage(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
