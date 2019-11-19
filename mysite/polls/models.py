from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length= 100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length= 200)
    votes = models.IntegerField(default= 0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text

class Company(models.Model):
    name = models.CharField(max_length= 100)
    address= models.CharField(max_length= 200)
    telephone = models.IntegerField()
    email = models.CharField(max_length= 50)
    fax = models.IntegerField()
    vat_number = models.IntegerField()

    def __str__(self):
        return self.name
