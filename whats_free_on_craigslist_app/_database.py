from whats_free_on_craigslist_app import models


def db_initialize_tables():
    models.Listing.objects.all().delete()
    models.Search.objects.all().delete()


def db_store_search(search):
    models.Search.objects.create(
        location=search['location'],
        search=search['search'],
        result_index=search['result_index'],
    )


def db_get_latest_search():
    return models.Search.objects.latest()


def db_store_listings(listings):
    # save each listing to database
    for listing in listings:
        models.Listing.objects.create(
            title=listing['title'],
            url=listing['url'],
            image_url=listing['image_url'],
            hood=listing['hood'],
        )


def db_get_all_listings():
    return models.Listing.objects.get_queryset().order_by('id')
