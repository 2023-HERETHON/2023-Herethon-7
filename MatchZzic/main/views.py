from django.shortcuts import redirect, render
from .models import Post

# Create your views here.
def main(request):
    return render(request, 'main.html')

def createform(request):
    if request.method == 'POST':
        place = Post()
        place.place = request.POST['place']
        place.save()
        
        return redirect('main')