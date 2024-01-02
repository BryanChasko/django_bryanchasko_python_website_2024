from django.shortcuts import render

def hello_world_view(request):
    context = {'message': 'Hello, World!'}
    return render(request, 'bryanchasko_website/index.html', context)