from django.contrib import admin
from .models import  Exam,Exam2,Exam3,Exam4
# Register your models here.

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('id','Question','Option1','Option2','Option3','Option4','Corrans')

@admin.register(Exam2)
class Exam2Admin(admin.ModelAdmin):
    list_display = ('Question','Option1','Option2','Option3','Option4','Corrans')

@admin.register(Exam3)
class Exam3Admin(admin.ModelAdmin):
    list_display = ('Question','Option1','Option2','Option3','Option4','Corrans')

@admin.register(Exam4)
class Exam4Admin(admin.ModelAdmin):
    list_display = ('Question','Option1','Option2','Option3','Option4','Corrans')