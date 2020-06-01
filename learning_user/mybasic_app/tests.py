from django.test import TestCase
from django.urls import reverse

from mybasic_app.models import (ToDolist, Item,
	Chercheur,Evaluateur,Commite)

from django.test import TestCase

# Index page
    # test that index page returns a 200

# Detail Page
    # test that detail page returns a 200 if the item exists
    # test that detail page returns a 404 if the item does not exist

# Booking Page
    # test that a new booking is made
    # test that a booking belongs to a contact
    # test that a booking belongs to an album
    # test that an album is not available after a booking is made



class MyHomePageTest(TestCase):


    # test that index returns a 200
# tsema kon kyn problem ygolke   f test t3k 
    def test_index_page(self):
        # you must add a name to index view: `name="index"`
        response = self.client.get(reverse('homme'))
        self.assertEqual(response.status_code, 200)


# test unitaire avec detaile page

''' 

 class DetailPageTest(TestCase):

    # test that detail page returns a 200 if the item exists
       # ran before each test.

    def setUp(self):
        impossible = Album.objects.create(title="Transmission Impossible")
        self.album = Album.objects.get(title='Transmission Impossible')

    # test that detail page returns a 200 if the item exists
    def test_detail_page_returns_200(self):
        album_id = self.album.id
        response = self.client.get(reverse('chercheur:beginchrch', args=(album_id,)))
        self.assertEqual(response.status_code, 200)

    # test that detail page returns a 404 if the items does not exist
    def test_detail_page_returns_404(self):
        album_id = self.album.id + 1
         #nmdelhe haja mknch mnha ygoli 404 pas existe
        response = self.client.get(reverse('store:detail', args=(album_id,)))
        self.assertEqual(response.status_code, 404)
'''