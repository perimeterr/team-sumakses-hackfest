from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from .models import ResourceListing, MaterialCategory, ResourceMaterial
from .forms import ResourceListingForm, MaterialCategoryForm, ResourceMaterialForm, SignInForm, SignUpForm

def sign_up(request):
    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            user = sign_up_form.save()
            # Optionally log the user in immediately after signup
            # login(request, user)
            return JsonResponse({'status': 'success', 'message': 'User registered successfully'}, status=201)
        else:
            return JsonResponse({'status': 'error', 'errors': sign_up_form.errors}, status=400)
    else:
        # For a React frontend, you likely won't render a signup form directly from Django.
        # You might just indicate that this endpoint is for POST requests.
        return JsonResponse({'message': 'Signup endpoint for POST requests'}, status=405)

def sign_in(request):
    if request.method == 'POST':
        sign_in_form = SignInForm(request.POST)
        if sign_in_form.is_valid():
            username = sign_in_form.cleaned_data['username']
            password = sign_in_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'status': 'success', 'message': 'Login successful'}, status=200)
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid username or password'}, status=401)
        else:
            return JsonResponse({'status': 'error', 'errors': sign_in_form.errors}, status=400)
    else:
        # For a React frontend, you likely won't render a signin form directly from Django.
        # You might just indicate that this endpoint is for POST requests.
        return JsonResponse({'message': 'Signin endpoint for POST requests'}, status=405)

def sign_out(request):
    logout(request)
    return JsonResponse({'status': 'success', 'message': 'Logout successful'}, status=200)

@login_required
def resource_listing_list(request):
    '''
    API endpoint to list all resource listings.
    '''
    resource_listings = ResourceListing.objects.all()
    serialized_listings = serializers.serialize('json', resource_listings)
    return JsonResponse({'resource_listings': serialized_listings}, safe=False)

@login_required
def resource_listing_detail(request, pk):
    '''
    API endpoint to display a single resource listing and its related materials.
    '''
    resource_listing = get_object_or_404(ResourceListing, pk=pk)
    resource_materials = ResourceMaterial.objects.filter(resource_listing=resource_listing)

    serialized_listing = serializers.serialize('json', [resource_listing])
    serialized_materials = serializers.serialize('json', resource_materials)

    return JsonResponse({'resource_listing': serialized_listing, 'resource_materials': serialized_materials}, safe=False)

@login_required
def create_resource_listing(request):
    '''
    API endpoint for creating resource listings, material categories, and resource materials.
    Handles POST requests for adding each.
    '''
    if request.method == 'POST':
        if 'add_resource_listing' in request.POST:
            resource_listing_form = ResourceListingForm(request.POST)
            if resource_listing_form.is_valid():
                resource_listing = resource_listing_form.save(commit=False)
                resource_listing.provider = request.user
                resource_listing.save()
                return JsonResponse({'status': 'success', 'message': 'Resource listing created successfully', 'id': resource_listing.id}, status=201)
            else:
                return JsonResponse({'status': 'error', 'errors': resource_listing_form.errors}, status=400)

        elif 'add_material_category' in request.POST:
            material_category_form = MaterialCategoryForm(request.POST)
            if material_category_form.is_valid():
                material_category = material_category_form.save()
                return JsonResponse({'status': 'success', 'message': 'Material category created successfully', 'id': material_category.id, 'name': material_category.name}, status=201)
            else:
                return JsonResponse({'status': 'error', 'errors': material_category_form.errors}, status=400)

        elif 'add_resource_material' in request.POST:
            resource_material_form = ResourceMaterialForm(request.POST)
            if resource_material_form.is_valid():
                resource_material = resource_material_form.save()
                return JsonResponse({'status': 'success', 'message': 'Resource material added successfully', 'id': resource_material.id}, status=201)
            else:
                return JsonResponse({'status': 'error', 'errors': resource_material_form.errors}, status=400)

    # For GET requests, you might want to return the forms for the frontend to render
    resource_listing_form = ResourceListingForm()
    material_category_form = MaterialCategoryForm()
    resource_material_form = ResourceMaterialForm()
    serialized_resource_listing_form = {name: field.label for name, field in resource_listing_form.fields.items()}
    serialized_material_category_form = {name: field.label for name, field in material_category_form.fields.items()}
    serialized_resource_material_form = {name: field.label for name, field in resource_material_form.fields.items()}

    return JsonResponse({
        'resource_listing_form': serialized_resource_listing_form,
        'material_category_form': serialized_material_category_form,
        'resource_material_form': serialized_resource_material_form
    })

# You might need separate endpoints for adding/updating/deleting related entities
# For example, to add a material to a specific resource listing:
@login_required
def add_material_to_listing(request, listing_pk):
    '''
    API endpoint to add a material to a specific resource listing.
    '''
    resource_listing = get_object_or_404(ResourceListing, pk=listing_pk)
    if request.method == 'POST':
        resource_material_form = ResourceMaterialForm(request.POST)
        if resource_material_form.is_valid():
            resource_material = resource_material_form.save(commit=False)
            resource_material.resource_listing = resource_listing
            resource_material.save()
            serialized_material = serializers.serialize('json', [resource_material])
            return JsonResponse({'status': 'success', 'message': 'Material added to listing', 'resource_material': serialized_material}, status=201)
        else:
            return JsonResponse({'status': 'error', 'errors': resource_material_form.errors}, status=400)
    else:
        resource_material_form = ResourceMaterialForm()
        serialized_form = {name: field.label for name, field in resource_material_form.fields.items()}
        return JsonResponse({'resource_material_form': serialized_form})

# Similarly, you would create endpoints for updating and deleting listings and materials.