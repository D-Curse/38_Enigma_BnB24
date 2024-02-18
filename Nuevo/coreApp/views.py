from django.shortcuts import render, get_object_or_404
from adminApp.models import Person
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def dashboard(request):
    people = Person.objects.all()
    all_skills = set()
    
    for person in people:
        skills = person.skills.split(', ')
        all_skills.update(skills)

    return render(request, 'core/dashboard.html', {'people': people, 'all_skills': all_skills})

@csrf_exempt
def filter_people(request):
    if request.method == 'POST':
        selected_skills = request.POST.getlist('skills[]')  # Assuming skills is a list
        filtered_people = Person.objects.filter(skills__in=selected_skills)

        # Return a JSON response with the filtered data directly as an array
        filtered_data = [{'name': person.name, 'qualifications': person.qualifications, 'experience': person.experience, 'skills': person.skills, 'phone_number': person.phone_number} for person in filtered_people]

        return JsonResponse({'filtered_data': filtered_data})

    return JsonResponse({'error': 'Invalid request method'})

def profile_view(request, user_id):
    person = get_object_or_404(Person, id=user_id)
    
    profile_data = {
        'name': person.name,
        'qualifications': person.qualifications,
        'experience': person.experience,
        'skills': person.skills,
        'phone_number': person.phone_number,
    }

    return render(request, 'core/profile_template.html', {'profile_data': profile_data})