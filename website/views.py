from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import New 
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

class NewListView(ListView):
    model = New
    queryset = New.objects.filter(status=1).order_by('-date_created')
    template_name = 'website/index.html'
    context_object_name = 'news'
    ordering = ['-date_created'] 
    paginate_by = 3


def contact(request):
    return render(request, 'website/contact.html', {'title': 'Contact'})