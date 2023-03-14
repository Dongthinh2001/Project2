from django.shortcuts import render


from django.shortcuts import get_object_or_404, render


def index(request):
    # question = get_object_or_404(Question, pk=question_id)
    return render(request, 'orders/index.html')
