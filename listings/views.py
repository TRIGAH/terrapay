from django.shortcuts import render, get_object_or_404
from .models import LandListing

# Create your views here.
def land_list(request):
    lands = LandListing.objects.all()
    return render(request, 'listings/land_list.html', {'lands': lands})

def land_detail(request, pk):
    land = get_object_or_404(LandListing, pk=pk)
    return render(request, 'listings/land_detail.html', {'land': land})
