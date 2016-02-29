from django.contrib import admin

# Register your models here.

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields': ['question_text']}),
            ('Date information', {'fields': ['published'], 'classes': ['collapse']}),
            ]
    list_display = ('question_text', 'published')
    list_filter = ['published']
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

