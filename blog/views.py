from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from blog.models import *
from calendar import month_name
from django.forms import ModelForm
from django.http import HttpResponseRedirect, HttpResponse
#from django.core.context_processor import csrf
from django.template.context_processors import csrf
import time

# Create your views here


class FormularioComentario(ModelForm):
    class Meta:
        model = Comentario
        exclude = ['idEntrada']


def comentario(request, pk):
    p = request.POST
    if 'mensaje' in p:
        autor = 'Anonimo'
        if p['autor']:
            autor = p['autor']

        comentario = Comentario(idEntrada=Entrada.objects.get(pk=pk))
        cf = FormularioComentario(p, instance=comentario)
        cf.fields['autor'].requried = False
        comentario = cf.save(commit=False)
        comentario.autor = autor
        comentario.save()

    return HttpResponseRedirect(reverse('blog.views.entrada', args=[pk]))


def mkmonth_lst():
    if not Entrada.objects.count(): return[]
    year, month = time.localtime()[:2]
    first = Entrada.objects.order_by('fecha')[0]
    fyear = first.fecha.year
    fmonth = first.fecha.month
    months = []

    for y in range(year, fyear-1, -1):
        star,end = 12, 0
        if y == year:
            star = month
        if y == fyear:
            end = fmonth-1

        for m in range(star,end, -1):
            months.append((y, m, month_name[m]))

    return months


def month(request, year, month):
    entrada = Entrada.objects.filter(fecha__year=year, fecha__month=month)
    diccionarioM = {
            'entrada_list': entrada,
            'user': request.user,
            'month': mkmonth_lst(),
            'archive': True,
            }
    return render_to_response('listado.html', diccionarioM)


def entrada(request,pk):

    idEntrada = Entrada.objects.get(pk=int(pk))
    comentario = Comentario.objects.filter(idEntrada=idEntrada)
    diccionario = {

            'variable': idEntrada,
            'usuario': request.user,
            'comentario': comentario,
            'form': FormularioComentario(),

            }

    diccionario.update(csrf(request))
    return render_to_response("entrada.html", diccionario)


def main(request):

    entrada = Entrada.objects.all().order_by("-fecha")
    paginator = Paginator(entrada,3)

    diccionario = {
            'articulos': entrada,
            'usuario': request.user.id,
            'months': mkmonth_lst(),
            'entrada_list': ''
            }

    try: pagina = int(request.GET.get("page", "1"))
    except ValueError: pagina = 1

    try:
        diccionario['articulos'] = paginator.page(pagina)
    except (InvalidPage, EmptyPage):
        diccionario['articulos'] = paginator.page(paginator.num_pages)


    return render_to_response("listado.html", diccionario)
