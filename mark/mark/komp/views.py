from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import context
from django.shortcuts import render_to_response
from .models import Buy, Author
from django.shortcuts import get_object_or_404
from .forms import RequestForm, AuthorForm

# Create your views here.

def request_details(request, id = None):
    instance = get_object_or_404(Buy, id = id)
    context = {'title':'Buy.title', 'instance':instance}
    return render(request, 'request.detail.html', context)

def request_create(request):
    form = RequestForm()
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        timestamp = request.POST.get('timestamp')
        status = request.POST.get('status')
        status1 = request.POST.get('status1')
        status2 = request.POST.get('status2')
        Buy.objects.create(title=title, content=content, timestamp=timestamp, status=status, status1=status1, status2=status2)
    context = {'form':form}
    return render(request,'request.create.html', context)

def request_list(request):
    queryset = Buy.objects.all()
    context = {'queryset':queryset, 'title':'Requests list'}
    return render(request, 'index.html', context)

def author_create(request):
    form = AuthorForm()
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        second_name = request.POST.get('second_name')
        email = request.POST.get('email')
        Author.objects.create(first_name=first_name, second_name=second_name, email=email)
    context = {'form':form}
    return render(request,'author.create.html', context)
