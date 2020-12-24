from django.shortcuts import render
from django.views import View
from whats_free_on_craigslist_app._craigslist import *
from whats_free_on_craigslist_app._database import *
from whats_free_on_craigslist_app._paginator import *


# HOME PAGE VIEW
def home_view(request):
    locations = craigslist_get_geo_locations()
    frontend = {
        'locations': locations,
    }
    return render(request, "whats_free_on_craigslist_app/home.html", frontend)


# LISTING PAGE VIEW
class ListingView(View):
    @staticmethod
    def post(request):
        # REINITIALIZE Listings and Searches TABLE IN SQLITE DB
        db_initialize_tables()

        # CREATE SEARCH OBJECT FROM POST DATA
        new_search = {
            'location': request.POST.get('location'),
            'search': request.POST.get('search', ""),
            'result_index': 0,
        }

        # STORE SEARCH TO DB
        db_store_search(new_search)

        # (handshake) GET LATEST SEARCH OBJECT FROM DB - should be the same as "new_search_obj" created above
        search = db_get_latest_search()

        # SEARCH CRAIGSLIST WITH URL - GET LISTINGS OBJECT
        new_listings, total_results = craigslist_search(craigslist_create_search_url(search))

        # STORE NEW LISTINGS TO DB
        db_store_listings(new_listings)

        # (handshake) GET LISTINGS FROM DB
        listings = db_get_all_listings()

        # SETUP PAGINATOR - page_number = 1
        page_obj = paginator_get_page_obj(listings, 1)

        # GET GEO LOCATIONS FOR DROPDOWN
        locations = craigslist_get_geo_locations()

        if search.search == "":
            search.search = 'all'

        frontend = {
            'search': search.search,
            'listings': listings,
            'set_location': search.location,
            'locations': locations,
            'page_obj': page_obj,
            'total_results': total_results,
        }
        # RENDER RESULTS
        return render(request, "whats_free_on_craigslist_app/listings.html", frontend)

    @staticmethod
    def get(request):
        # GET NEW PAGE NUMBER FROM HTTP GET REQUEST
        page_number = request.GET.get('page')

        # GET LISTINGS FROM DB
        listings = db_get_all_listings()

        # SETUP PAGINATOR
        page_obj = paginator_get_page_obj(listings, page_number)

        # CHECK IF PAGE OBJECT HAS NEXT - Try Search
        if page_obj.has_next() is False:
            # GET LATEST SEARCH OBJECT
            search_obj = db_get_latest_search()

            # UPDATE SEARCH OBJECT
            updated_search_obj = {
                'location': search_obj.location,
                'search': search_obj.search,
                'result_index': str(int(search_obj.result_index) + 120),
            }

            # STORE UPDATED SEARCH OBJECT TO DB
            db_store_search(updated_search_obj)

            # (handshake) GET LATEST SEARCH OBJECT FROM DB - should be the same as "updated_search_obj" created above
            search = db_get_latest_search()

            # SEARCH CRAIGSLIST WITH URL - GET NEW LISTINGS OBJECT
            new_listings, total_results = craigslist_search(craigslist_create_search_url(search))

            # STORE NEW LISTINGS TO DB
            db_store_listings(new_listings)

            # (handshake) GET LISTINGS FROM DB
            listings = db_get_all_listings()

            # SETUP PAGINATOR
            page_obj = paginator_get_page_obj(listings, page_number)

        frontend = {
            'page_obj': page_obj,
        }
        return render(request, "whats_free_on_craigslist_app/listings.html", frontend)
