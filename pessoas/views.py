from django.template import loader
from django.http import HttpRequest, HttpResponse

from pessoas.services import PessoaRn

def index(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("pessoas/index.html")
    people_list = PessoaRn.objects.all()
    context = {'people_list': people_list}
    return HttpResponse(template.render(context, request))
