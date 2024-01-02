from django.shortcuts import render
from django.views import generic
from .models import UserPost, UserComments


class UserPost(generic.ListView):
    model = UserPost
    queryset = UserPost.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6
    
    
def home(request):
    return render(request, 'index.html')   

