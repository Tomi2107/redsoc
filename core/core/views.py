from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth import logout



class HomeView(View):
    def get(self, request, *args, **kwargs):
        
        context={

        }
        return render(request, 'pages/index.html', context)
    
# def Logout(request):
#     logout(request)
#     return render(request, 'pages/index.html')