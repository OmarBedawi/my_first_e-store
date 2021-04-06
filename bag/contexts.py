from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from ebooks.models import Ebook, Ebook_reader


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        try:
            ebook = get_object_or_404(Ebook, pk=item_id)
        except:
            ebook = get_object_or_404(Ebook_reader, pk=item_id)
        total += quantity * ebook.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'ebook': ebook,
        })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
