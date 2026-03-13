from django.shortcuts import render, redirect, get_object_or_404
from .models import GradeEntry
from .forms import GradeEntryForm


def score_view(request):
    entries = GradeEntry.objects.all()

    if request.method == "POST":
        form = GradeEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('score_view')
    else:
        form = GradeEntryForm()

    return render(request, 'score_list.html', {'form': form, 'entries': entries})


def edit_score(request, score_id):
    entry = get_object_or_404(GradeEntry, id=score_id)

    if request.method == "POST":
        form = GradeEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('score_view')
    else:
        form = GradeEntryForm(instance=entry)

    return render(request, 'score_edit.html', {'form': form, 'entry': entry})


def delete_score(request, score_id):
    entry = get_object_or_404(GradeEntry, id=score_id)
    entry.delete()
    return redirect('score_view')

