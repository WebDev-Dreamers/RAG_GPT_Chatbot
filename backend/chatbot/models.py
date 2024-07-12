from django.db import models

# Create your models here.

# 대화를 기억할 History 모델 선언
class History(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    question = models.TextField()
    answer = models.TextField()
    
    def __str__(self):
        return f"Date: {self.datetime}     Q: {self.question}    Answer: {self.answer}"
    
    class Meta:
        db_table = 'history'