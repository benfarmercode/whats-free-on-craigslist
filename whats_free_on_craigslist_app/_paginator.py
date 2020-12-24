from django.core.paginator import Paginator

items_per_page = 60 #must be less than 120


def paginator_get_page_obj(listings, page):
    paginator = Paginator(listings, items_per_page)
    return paginator.get_page(page)


def paginator_get_items_per_page():
    return items_per_page
