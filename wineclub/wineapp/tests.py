from django.test import TestCase
from .models import WineType, Wine, Winery, WineReview, Event
from .forms import EventForm, ReviewForm
from django.urls import reverse

# test WineType class
class WineTypeTest(TestCase):
    def test_stringOutput(self):
        winetype=WineType(typename='Syrah')
        self.assertEqual(str(winetype), winetype.typename)
    def test_tablename(self):
        self.assertEqual(str(WineType._meta.db_table), 'winetype')
 
# test Winery class
class WineryTest(TestCase):
    def test_stringOutput(self):
        winery=Winery(wineryname='My Winery')
        self.assertEqual(str(winery), winery.wineryname)
    def test_tablename(self):
        self.assertEqual(str(Winery._meta.db_table), 'winery')
   
# test Event class
class WineTest(TestCase):
    def test_stringOutput(self):
        wine=Wine(winename='My Red Wine')
        self.assertEqual(str(wine), wine.winename)
    def test_tablename(self):
        self.assertEqual(str(Wine._meta.db_table), 'wine')

# test index view
class TestIndexView(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'wineapp/index.html')
 
# test events view
class TestEventView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/wineapp/events')
        self.assertEqual(response.status_code, 200)
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('events'))
        self.assertEqual(response.status_code, 200)
    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('events'))
        self.assertTemplateUsed(response, 'wineapp/events.html')

# test add event form
class New_Event_Form_Test(TestCase):
    def test_eventForm_is_valid(self):
        form = EventForm(data={'eventtitle': "white wine tasting", 'eventlocation': "park", 'eventdate': "2019-03-31", 'eventdescription':"Taste some wines in the park" })
        self.assertTrue(form.is_valid())
    def test_eventForm_invalid(self):
        form = EventForm(data={'eventtitle': "white wine tasting", 'eventlocation': "park", 'eventdate': "2019-03-31", 'eventdescription':"Taste some wines in the park" })
        self.assertFalse(form.is_valid())
