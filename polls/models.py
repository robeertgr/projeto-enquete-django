from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200) # campo de caracteres
    pub_date = models.DateTimeField('Date published') # data de publicação

    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    # toda alternativa tem que vincular a uma pergunta, uma relação entre 2 tabelas
    # on_delete serve para quando apagar uma pergunta, apagar as alternativas também
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) # campo de inteiros, com padrão = 0

    def __str__(self) -> str:
        return self.choice_text