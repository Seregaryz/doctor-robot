from django.db import models


class Symptom(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название симптома")

    def __str__(self):
        return self.name


class Disease(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название болезни")
    symptom = models.ManyToManyField(
        Symptom,
        through='Specification',
    )

    def __str__(self):
        return self.name


class Specification(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    factor = models.IntegerField()

    def __str__(self):
        return f'{self.disease.name}-{self.symptom.name} {self.factor}'

