from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# ChoiceInline allows adding/editing choices directly inside a Question
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


# QuestionInline allows adding/editing questions directly inside a Course
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


# QuestionAdmin includes ChoiceInline to manage choices alongside questions
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['content']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# Register models with Django Admin
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)