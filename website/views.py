from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from .models import New 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

news = [
    {
        'title': 'Summer',
        'author': 'Diego',
        'content': 'Summer content',
        'date_created': 'July 12, 2022'
        }
    ,
    {'title': 'Brunch',
        'author': 'Dany',
        'content': 'Brunch content',
        'date_created': 'July 13, 2022'

    }


]
def index(request):
    context ={
        'news': news
    }
    return render(request, 'website/index.html', context)

class NewListView(generic.ListView):
    model = New
    queryset = New.objects.filter(status=1).order_by('-date_created')
    template_name = 'website/index.html'
    context_object_name = 'news'
    ordering = ['-date_created'] 
    paginate_by = 3


def contact(request):
    return render(request, 'website/contact.html', {'title': 'Contact'})

def signUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}! Your account has been created')
            return redirect('website-index')

    else:
        form = UserCreationForm()
    return render(request, 'website/signup.html', {'form': form} )