from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView,DeleteView, View
from .models import Note, NoteComment
from .models import Note
from .forms import NoteForm
from django.urls import reverse_lazy

"""
Class-based views:

View        = generic view
ListView    = get a list of records
DetailView  = get a single(detail) record
CreateView  = create a new record
DeleteView  = remove a record
UpdateView  = modify an existing record
LoginView   = login
"""
# create class views here.
class NoteWebsite(View):
     model = Note
     template_name = "notes/website.html"

class NoteList(ListView):
    model = Note
    template_name = "notes/list.html"

class NoteCreate (CreateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/create.html"
    success_url = reverse_lazy('note_list')


class NoteDetail(DetailView):
    model = Note
    template_name = "notes/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # load all comment for this note
        note = self.object
        comments = NoteComment.objects.filter(note=note).prefetch_related("author")
        context["comments"] = comments
        return context
    
      

class NoteUpdate(UpdateView):
    model = Note
    form_class =NoteForm
    template_name = "notes/create.html"
    success_url =reverse_lazy('note_list')

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return super().get_context_data(**kwargs)

class NoteDelete(DeleteView):
    model = Note
    template_name = "notes/delete.html"
    success_url = reverse_lazy('note_list')





