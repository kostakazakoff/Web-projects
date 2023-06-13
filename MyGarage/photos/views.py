from django.shortcuts import render, redirect
from .forms import CreatePhotoForm


def add_photo(request):
    if request.method == 'POST':
        form = CreatePhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CreatePhotoForm()
    
    # TODO: return to add vehicle page, keeping vehicle input data
    
    context = {'title': 'Add photo', 'form': form}
    return render(request, 'photos/add-photo.html', context)

def details_photo(request, pk):
    return render(request, 'photos/details-photo.html')

def delete_photo(request, pk):
    return render(request, 'photos/delete-photo.html')
