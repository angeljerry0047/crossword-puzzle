from django.shortcuts import render
from .models import Clue, Puzzle, Entry

# Create your views here.
def drill(request):
    if(request.method=='POST'):
        entryId = Clue.objects.filter(clue_text=request.POST['answer']).select_related()
        return render(request, 'xword_data/xword-answer.html', {'data':entryId})
    # find_list = Entry.objects.order_by("?").first()
    else :
        find_list = Clue.objects.order_by("?").first()
        context = {'data': find_list}
        return render(request, 'xword_data/xword-drill.html', context)

def answer(request):
    data = 'sample data'
    context = {'data': data}
    return render(request, 'xword_data/xword-answer.html', context)
