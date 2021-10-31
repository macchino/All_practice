from django.shortcuts import redirect, render

from boards.models import Themes
from . import forms
from .models import Themes
from django.contrib import messages

def create_theme(request):
    create_theme_form = forms.CreateThemeForm(request.POST or None)
    if create_theme_form.is_valid():
        create_theme_form.instance.user = request.user
        create_theme_form.save()
        messages.success(request, '掲示板が作成されました。')
        return redirect('boards:list_themes')
    return render(
        request, 'boards/create_theme.html', context={
            'create_theme_form': create_theme_form,
        }
    )

def list_themes(request):
    themes = Themes.objects.fetch_all_themes()
    return render(request, 'boards/list_themes.html', context={
        'themes': themes
    })
