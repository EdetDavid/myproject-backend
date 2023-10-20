from rest_framework.views import APIView
from rest_framework.response import Response
from .algorithm import GeneticAlgorithmService
from .models import *
from .serializers import *
from rest_framework import viewsets
from django.contrib.auth.models import User
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.authentication import TokenAuthentication


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class Individuals(APIView):
    def get(self, request):
        individual = Individual.objects.all()
        serializer = IndividualSerializer(individual, many=True)
        return Response(serializer.data)

    def post(self, request):
        population_size = int(request.data.get('population_size'))
        num_generations = int(request.data.get('num_generations'))
        num_selected = int(request.data.get('num_selected'))
        mutation_rate = float(request.data.get('mutation_rate'))
        gene_length = int(request.data.get('gene_length'))

        algorithm = GeneticAlgorithmService(population_size, gene_length)
        population = algorithm.initialize_population()

        for generation in range(num_generations):
            for individual in population:
                individual.fitness_score = algorithm.calculate_fitness(
                    individual)
                individual.generation = generation

                individual.save()

            population = algorithm.evolve_population(
                population, num_selected, mutation_rate)

        individuals = Individual.objects.all().values('has_albinism')

        return Response({'message': 'Genetic algorithm completed successfully.', 'individuals': individuals})
