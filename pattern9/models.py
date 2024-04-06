from django.db import models
class Question(models.Model):
    q_no = models.IntegerField(default=1)
    question = models.TextField(blank=True)
    answer=models.IntegerField(blank=False,default=1)
    correct = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)
    accuracy = models.FloatField(default=0)
    modal = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.q_no)

    def calcAccu(self):
        self.accuracy = round(self.correct / (float(self.correct + self.wrong)), 2) * 100

    def answered(self, right=1):
        if right:
            self.correct = self.correct + 1
        else:
            self.wrong = self.wrong + 1
        self.calcAccu()
        self.save()