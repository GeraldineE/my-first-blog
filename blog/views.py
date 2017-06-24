from django.shortcuts import render

#El metodo post_list recibe una peticion request
#metodo render renderiza(construye) la plantilla
def post_list(request):
    return render(request, 'blog/post_list.html', {})
