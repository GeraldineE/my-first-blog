from django.shortcuts import render
from .models import Post
from django.utils import timezone

#El metodo post_list recibe una peticion request
#metodo render renderiza(construye) la plantilla
def post_list(request):
    posts= Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
