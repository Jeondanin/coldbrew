from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    context = {
        'message' : '은비는 소중해',
        'content' : '공부하자 모두들',
    }
    return render("index.html", context)

def Register(request):
    print(request)
    return JsonResponse({'success':"ok"})