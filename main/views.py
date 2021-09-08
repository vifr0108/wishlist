from django.shortcuts import render, get_object_or_404

from .models import WishList


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {"title": "Wishlist | about project"})


def list_page(request, pk):
    """
    FBV - views основаны на функциях
    СBV - views основаны на классах
    """
    # print('[PK]', pk)
    # wishlist = WishList.objects.get(pk=pk)
    wishlist = get_object_or_404(WishList, pk=pk)

    print([wishlist], wishlist)
    return render(request,
                  'wish_list.html',
                  {'wishlist': wishlist,
                   'is_owner_list': wishlist.owner == request.user})
