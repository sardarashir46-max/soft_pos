
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Category
from .forms import CategoryForm


# CREATE + READ + SEARCH
def category_list(request):

    if request.method == 'POST':

        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Category created successfully!'
            )

            return redirect('category_list')

        else:
            messages.error(
                request,
                'Please correct the form errors.'
            )

    else:
        form = CategoryForm()

    search_query = request.GET.get('search', '')

    categories = Category.objects.all().order_by('-id')

    if search_query:
        categories = categories.filter(
            name__icontains=search_query
        )

    total_categories = Category.objects.count()

    active_categories = Category.objects.filter(
        status=True
    ).count()

    inactive_categories = Category.objects.filter(
        status=False
    ).count()

    context = {
        'form': form,
        'categories': categories,
        'search_query': search_query,
        'total_categories': total_categories,
        'active_categories': active_categories,
        'inactive_categories': inactive_categories,
    }

    return render(
        request,
        'categories/category_list.html',
        context
    )


# UPDATE
def category_edit(request, pk):

    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':

        form = CategoryForm(
            request.POST,
            instance=category
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Category updated successfully!'
            )

            return redirect('category_list')

    else:
        form = CategoryForm(instance=category)

    return render(
        request,
        'categories/category_edit.html',
        {
            'form': form,
            'category': category
        }
    )


# DELETE
def category_delete(request, pk):

    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':

        category_name = category.name

        category.delete()

        messages.success(
            request,
            f'{category_name} deleted successfully!'
        )

        return redirect('category_list')

    return render(
        request,
        'categories/category_confirm_delete.html',
        {
            'category': category
        }
    )
