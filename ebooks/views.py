from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Ebook, Category

# Create your views here.


def all_ebooks(request):
    """ A view to show all ebooks, including sorting and search queries """

    ebooks = Ebook.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            ebooks = ebooks.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)



        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('ebooks'))

            queries = Q(title__icontains=query) | Q(description__icontains=query)
            ebooks = ebooks.filter(queries)


    context = {
        'ebooks': ebooks,  # pylint: disable=no-member
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'ebooks/ebooks.html', context)


def ebook_detail(request, ebook_id):
    """ A view to show individual ebook details """

    ebook = get_object_or_404(Ebook, pk=ebook_id)

    context = {
        'ebook': ebook,  # pylint: disable=no-member
    }

    return render(request, 'ebooks/ebook_detail.html', context)
