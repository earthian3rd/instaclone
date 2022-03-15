from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed

# Create your views here.

class Home(APIView):
    def get(self, request):
        context = {}
        template = 'main.html'
        
        feeds= Feed.objects.all().order_by('-id')
        context = {'feeds': feeds}
        return render(request, template, context)