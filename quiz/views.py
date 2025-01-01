from django.shortcuts import render

def quiz_list(request):
    return render(request, 'quiz_list.html', {})

