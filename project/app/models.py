# from django.db import models

# class Amostra(models.Model):
#     codigo = models.CharField(max_length=20)

#     def __str__(self):
#         return self.codigo

# class Taxonomia(models.Model):
#     especie = models.CharField(max_length=50)

#     def __str__(self):
#         return self.especie

# class Frequencia(models.Model):
#     contagem = models.IntegerField()
#     especie =  models.ForeignKey(Taxonomia, on_delete=models.CASCADE)
#     amostra = models.ForeignKey(Amostra, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.contagem