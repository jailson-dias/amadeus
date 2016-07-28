from django.shortcuts import render


def usuario(request):
    context = {}
    # curso = Curso(request.POST or None,request.FILES or None)
    # if curso.is_valid():
    #     curso.save()
    #     context['sucesso'] = True
    #     curso = Curso()
    # context['curso'] = curso
    return render(request,"contas/usuario.html",context)
