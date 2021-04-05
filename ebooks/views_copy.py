from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Ebook, Category, Ebook_reader
from .forms import EbookForm, EbookForms

# Create your views here.


def all_ebooks(request):
    """ A view to show all ebooks, including sorting and search queries """

    ebooks = Ebook.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                ebooks = ebooks.annotate(lower_title=Lower('title'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            ebooks = ebooks.order_by(sortkey)

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

    current_sorting = f'{sort}_{direction}'

    context = {
        'ebooks': ebooks,  # pylint: disable=no-member
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'ebooks/ebooks.html', context)


def ebook_detail(request, ebook_id):
    """ A view to show individual ebook details """

    ebook = get_object_or_404(Ebook, pk=ebook_id)

    context = {
        'ebook': ebook,  # pylint: disable=no-member
    }

    return render(request, 'ebooks/ebook_detail.html', context)


def ebook_reader(request):
    """ A view to show all ebook readers, including sorting and search queries """

    ebook_readers = Ebook_reader.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'model':
                sortkey = 'lower_model'
                ebook_readers = ebook_readers.annotate(lower_model=Lower('model'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            ebook_readers = ebook_readers.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            ebook_readers = ebook_readers.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            queries = Q(title__icontains=query) | Q(description__icontains=query)
            # ebook_readers = ebook_readers.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'ebook_readers': ebook_readers,  # pylint: disable=no-member
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'ebooks/ebook_reader.html', context)


def ebook_reader_detail(request, ebook_reader_id):
    """ A view to show individual ebook reader details """

    ebook_reader = get_object_or_404(Ebook_reader, pk=ebook_reader_id)

    context = {
        'ebook_reader': ebook_reader,  # pylint: disable=no-member
    }

    return render(request, 'ebooks/ebook_reader_detail.html', context)


@login_required
def add_ebook(request):
    """ Add an e-book to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = EbookForm(request.POST, request.FILES)
        if form.is_valid():
            ebook = form.save()
            messages.success(request, 'Successfully added E-Book!')
            return redirect(reverse('ebook_detail', args=[ebook.id]))
        else:
            messages.error(request, 'Failed to add e-book. Please ensure the form is valid.')
    else:
        form = EbookForm()

    template = 'ebooks/add_ebook.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_ebook(request, ebook_id):
    """ Edit an e-book in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    ebook = get_object_or_404(Ebook, pk=ebook_id)
    if request.method == 'POST':
        form = EbookForm(request.POST, request.FILES, instance=ebook)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated E-book!')
            return redirect(reverse('ebook_detail', args=[ebook.id]))
        else:
            messages.error(request, 'Failed to update E-book!. Please ensure the form is valid.')
    else:
        form = EbookForm(instance=ebook)
        messages.info(request, f'You are editing {ebook.title}')

    template = 'ebooks/edit_ebook.html'
    context = {
        'form': form,
        'ebook': ebook,
    }

    return render(request, template, context)


@login_required
def delete_ebook(request, ebook_id):
    """ Delete an e-book from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    ebook = get_object_or_404(Ebook, pk=ebook_id)
    ebook.delete()
    messages.success(request, 'E-Book deleted!')
    return redirect(reverse('ebooks'))


@login_required
def add_ebook_reader(request):
    """ Add an e-book reader to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = EbookForms(request.POST, request.FILES)
        if form.is_valid():
            ebook_reader = form.save()
            messages.success(request, 'Successfully added E-Book Reader!')
            return redirect(reverse('ebook_reader_detail', args=[ebook_reader.id]))
        else:
            messages.error(request, 'Failed to add E-Book Reader. Please ensure the form is valid.')
    else:
        form = EbookForms()

    template = 'ebooks/add_ebook_reader.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_ebook_reader(request, ebook_reader_id):
    """ Edit an e-book reader in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    ebook_reader = get_object_or_404(Ebook_reader, pk=ebook_reader_id)
    if request.method == 'POST':
        form = EbookForms(request.POST, request.FILES, instance=ebook_reader)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated E-book Reader!')
            return redirect(reverse('ebook_reader_detail', args=[ebook_reader_id]))
        else:
            messages.error(request, 'Failed to update E-book Reader!. Please ensure the form is valid.')
    else:
        form = EbookForms(instance=ebook_reader)
        messages.info(request, f'You are editing {ebook_reader.model}')

    template = 'ebooks/edit_ebook_reader.html'
    context = {
        'form': form,
        'ebook_reader': ebook_reader,
    }

    return render(request, template, context)


@login_required
def delete_ebook_reader(request, ebook_reader_id):
    """ Delete an e-book reader from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    ebook_reader = get_object_or_404(Ebook_reader, pk=ebook_reader_id)
    ebook_reader.delete()
    messages.success(request, 'E-Book reader deleted!')
    return redirect(reverse('ebook_reader'))
