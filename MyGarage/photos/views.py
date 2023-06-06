from django.shortcuts import render, redirect


def add_photo(request, *args, **kwargs):
    if request.method == 'POST':
        # TODO: handle request
        return redirect('add vehicle')
    
    context = {'title': 'Add photo'}
    return render(request, 'photos/add-photo.html', context)

def details_photo(request, pk):
    return render(request, 'photos/details-photo.html')

def delete_photo(request, pk):
    return render(request, 'photos/delete-photo.html')
