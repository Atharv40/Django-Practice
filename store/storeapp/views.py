from django.shortcuts import render, get_object_or_404, redirect
from .models import Store
from .forms import StoreForm

def store_list_view(request):
    """
    Display the list of all stores.
    """
    stores = Store.objects.all()
    return render(request, 'store_list.html', {'stores': stores})

def store_detail_view(request, pk):
    """
    Display the details of a specific store.
    """
    store = get_object_or_404(Store, pk=pk)
    return render(request, 'store_detail.html', {'store': store})

def store_create_view(request):
    """
    Create a new store.
    """
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store-list')  # Redirect to the list view after creation
    else:
        form = StoreForm()
    return render(request, 'store_form.html', {'form': form, 'action': 'Create'})

def store_update_view(request, pk):
    """
    Update an existing store.
    """
    store = get_object_or_404(Store, pk=pk)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('store-list')  # Redirect to the list view after updating
    else:
        form = StoreForm(instance=store)
    return render(request, 'store_form.html', {'form': form, 'action': 'Update'})

def store_delete_view(request, pk):
    """
    Delete a store.
    """
    store = get_object_or_404(Store, pk=pk)
    if request.method == 'POST':
        store.delete()
        return redirect('store-list')  # Redirect to the list view after deletion
    return render(request, 'store_confirm_delete.html', {'store': store})
