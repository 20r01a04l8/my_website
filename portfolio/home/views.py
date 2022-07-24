from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('about')
      

def contact(request):
    # handling the form here
    if request.method == 'POST':
        print(request.POST['name'])
        print(request.POST['phone'])
    return render(request, 'contact.html')
