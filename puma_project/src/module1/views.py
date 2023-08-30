from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .models import UsersPuma
from django.http import JsonResponse

def print_ag_grid(request):
    """
    affichage avec aggrid
    """
    # recuperer toutes les données de la b
    # ase de données
    user_all = UsersPuma.objects.all()
    json_file = JsonResponse([user.serialize() for user in user_all], safe=False)
    #return json_file
    return render(request, "module1/print_with_ag_grid.html")