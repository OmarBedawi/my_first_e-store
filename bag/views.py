from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages

from ebooks.models import Ebook, Ebook_reader

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    try:
        ebook = get_object_or_404(Ebook, pk=item_id)
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, f'Updated  "{ebook.title}" quantity to {bag[item_id]}')  # noqa: disable=line-too-long
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added "{ebook.title}" to your bag')
    except Exception:
        ebook = get_object_or_404(Ebook_reader, pk=item_id)
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, f'Updated  "{ebook.brand} {ebook.model}" quantity to {bag[item_id]}')  # noqa: disable=line-too-long
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added "{ebook.brand} {ebook.model}" to your bag')  # noqa: disable=line-too-long

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    try:
        ebook = get_object_or_404(Ebook, pk=item_id)
        if quantity > 0:
            bag[item_id] = quantity
            messages.success
            (request, f'Updated  "{ebook.title}" quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed "{ebook.title}" from your bag')
    except Exception:
        ebook = get_object_or_404(Ebook_reader, pk=item_id)
        if quantity > 0:
            bag[item_id] = quantity
            messages.success
            (request, f'Updated  "{ebook.brand} {ebook.model}" quantity to {bag[item_id]}')  # noqa: disable=line-too-long
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed "{ebook.brand} {ebook.model}" from your bag')  # noqa: disable=line-too-long

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        ebook = get_object_or_404(Ebook, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed "{ebook.title}" from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception:
        ebook = get_object_or_404(Ebook_reader, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed "{ebook.brand} {ebook.model}" from your bag')  # noqa: disable=line-too-long

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
