from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def Register(request):
    print(request)
    return JsonResponse({'success':"ok"})