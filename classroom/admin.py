from django.contrib import admin
from .models import User, Subject, Quiz, Question, Answer, TakenQuiz, Student, StudentAnswer


admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(TakenQuiz)
admin.site.register(Student)
admin.site.register(StudentAnswer)
