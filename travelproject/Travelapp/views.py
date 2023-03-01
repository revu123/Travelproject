from django.shortcuts import render
from.models import Place
from.models import Team
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    char=Team.objects.all()
    return render(request,"index.html",{'result':obj,'result2':char})

