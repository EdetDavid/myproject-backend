from django.db import models

class Individual(models.Model):
    genes = models.CharField(max_length=255)
    fitness_score = models.FloatField(default=0.0)
    generation = models.IntegerField(default=0)
    has_albinism = models.BooleanField(default=False)


    def __str__(self):
        return self.genes
    
    
    

class OptimizationResult(models.Model):
    best_solution = models.JSONField()
    fitness = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Optimization Result {self.id}"
