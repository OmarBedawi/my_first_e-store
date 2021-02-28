from django.shortcuts import render
from .models import Ebook

# Create your views here.


def all_ebooks(request):
    """ A view to show all ebooks, including sorting and search queries """

    ebooks = Ebook.objects.all()

    context = {
        'ebooks': ebooks,  # pylint: disable=no-member
    }

    return render(request, 'ebooks/ebooks.html', context)
