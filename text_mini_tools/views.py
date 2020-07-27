from django.shortcuts import render
from .forms import TextField


def char_counter(request):
    count = 0
    if request.method == 'POST':
        text_field = TextField(request.POST)

        if text_field.is_valid():
            text = text_field.cleaned_data['text']

            count = len(text)
            print(text)

    text_field = TextField()
    return render(request, 'text_mini_tools/index.html', {'text_field': text_field, 'count': count})
