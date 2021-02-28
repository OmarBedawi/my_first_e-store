from django.shortcuts import render, get_object_or_404
from .models import Ebook

# Create your views here.


def all_ebooks(request):
    """ A view to show all ebooks, including sorting and search queries """

    ebooks = Ebook.objects.all()

    context = {
        'ebooks': ebooks,  # pylint: disable=no-member
    }

    return render(request, 'ebooks/ebooks.html', context)


def ebook_detail(request, ebook_id):
    """ A view to show individual ebook details """

    ebook = get_object_or_404(Ebook, pk=ebook_id)

    context = {
        'ebook': ebook,  # pylint: disable=no-member
    }

    return render(request, 'ebooks/ebook_detail.html', context)
