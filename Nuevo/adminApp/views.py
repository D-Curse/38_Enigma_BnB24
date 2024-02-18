from django.shortcuts import render
from django.http import HttpResponse
from faker import Faker
from .models import Person
import random

# Create your views here.

fake = Faker()

def generate_random_data(request):
    def generate_random_person():
        return Person(
            name=fake.name(),
            qualifications=random.choice(['Bachelor\'s Degree', 'Master\'s Degree', 'PhD', 'Associate Degree']),
            experience=random.randint(1, 20),
            skills=', '.join(fake.words(nb=random.randint(1, 5))),
            cultural_fit=random.choice(['Team Player', 'Inclusive', 'Adaptive', 'Collaborative', 'Open-minded', 'Cross-cultural', 'Respectful', 'Creative']),
            phone_number=fake.phone_number(),
            resume_path=f''
        )
    people_data = [generate_random_person() for _ in range(100)]
    Person.objects.bulk_create(people_data)

    return HttpResponse("Random data generated and added to the database.")

def delete_all_data(request):
    Person.objects.all().delete()

    return HttpResponse("Random data generated and added to the database.")

def display_people(request):
    people = Person.objects.all()
    return render(request, 'core/display_people.html', {'people': people})