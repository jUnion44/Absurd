from django.contrib import admin
from .models import *

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra=0
    fk_name  = "promptCurrent"

class PromptAdmin(admin.ModelAdmin):
    inlines = [
        ChoiceInline,
    ]

#Register your models here.
admin.site.register(Tag)
admin.site.register(Prompt,PromptAdmin)
admin.site.register(Choice)
