from django.http import HttpResponse
from django.shortcuts import render


from django.shortcuts import get_object_or_404, render


def index(request, id_pitch):
    # question = get_object_or_404(Question, pk=question_id)
    return render(request, 'orders/index.html', {"id_pitch": id_pitch})
    # return HttpResponse("You're voting on question %s." % id_pitch)
