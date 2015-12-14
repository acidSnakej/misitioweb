from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from blog.models import *
# Create your views here


def entrada(request,pk):
    idEntrada = Entrada.objects.get(pk=int(pk))
    return render_to_response("entrada.html",dict(entrada=idEntrada, usuario=request.user))


def main(request):
    entrada = Entrada.objects.all().order_by("-fecha")
    paginator = Paginator(entrada,3)

    try: pagina = int(request.GET.get("page","1"))
    except ValueError: pagina = 1

    try:
        entrada = paginator.page(pagina)
    except (InvalidPage,EmptyPage):
        entrada = paginator.page(paginator.num_pages)

    return render_to_response("listado.html",dict(entrada=entrada, usuario=request.user.id))
