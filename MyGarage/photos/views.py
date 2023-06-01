from django.shortcuts import render

def details_photo(request, pk):
    return render(request, 'photos/details-photo.html')

def add_photo(request):
    return render(request, 'photos/add-photo.html')

def delete_photo(request, pk):
    return render(request, 'photos/delete-photo.html')
