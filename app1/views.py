from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Hobby

def home(request):
    return render(request, 'home.html')

def hobbies(request):
    hobbies = Hobby.objects.order_by("date_added")
    context = {'hobbies': hobbies}
    return render(request, 'hobbies.html', context)

def hobby(request, hobby_id):
    """Show a single hobby and all its descriptions"""
    hobby = get_object_or_404(Hobby, id=hobby_id)
    # Retrieve the specific Hobby object by its ID. If it doesn't exist, return a 404 error.
    hobbydescriptions = hobby.hobbydescription_set.order_by("-date_added")
    # Get all HobbyDescription objects related to the Hobby, ordered by date added in descending order.
    context = {'hobby': hobby, 'hobbydescriptions': hobbydescriptions}
    # Create a context dictionary to pass the hobby and its descriptions to the template.
    return render(request, 'hobby.html', context)
    # Render the 'hobby.html' template with the context containing the hobby and its descriptions.
