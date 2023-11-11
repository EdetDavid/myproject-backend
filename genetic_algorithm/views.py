from .ga_logic import *
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .algorithm import GeneticAlgorithmService
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


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


class Optimize(APIView):
    def get(self, request):
        optimization_result = OptimizationResult.objects.all()
        serializer = OptimizationResultSerializer(
            optimization_result, many=True)
        return Response(serializer.data)

    def post(self, request):
        population_size = int(request.data.get('populationSize'))
        mutation_rate = float(request.data.get('mutationRate',))
        generations = int(request.data.get('generations'))

        # Load the dataset
        dataset = load_dataset()
        dataset_size = len(dataset)

        # Initialize the population
        population = initialize_population(population_size, dataset_size)

        # Genetic Algorithm optimization
        for _ in range(generations):
            fitness_scores = [fitness_function(
                ind, dataset) for ind in population]

            parents = [population[i]
                       for i in np.argsort(fitness_scores)[:2]]

            child = crossover(parents[0], parents[1])

            child = mutate(child, mutation_rate)

            replace_index = np.argmin(fitness_scores)
            population[replace_index] = child

        # Store the optimization result in the database
            best_solution = min(
                population, key=lambda ind: fitness_function(ind, dataset))
            fitness = fitness_function(best_solution, dataset)
            optimization_result = OptimizationResult.objects.create(
                best_solution=best_solution.tolist(),
                fitness=fitness
            )

            # Serialize and return the result
            serializer = OptimizationResultSerializer(optimization_result)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
