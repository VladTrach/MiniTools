from django.shortcuts import render


def char_counter(request):
    return render(request, 'text_mini_tools/index.html')
