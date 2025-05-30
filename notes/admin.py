from django.contrib import admin
from .models import Note, NoteComment

# Register your models here.
# admin.site.register(model_name)
admin.site.register(Note)
admin.site.register(NoteComment)