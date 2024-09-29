from django.test import TestCase, Client
from django.core.cache import cache
from django.urls import reverse
import requests_mock
from .config import api_key


class CalendarViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.api_url = "https://rekrutacja.teamwsuws.pl/events/"
        self.events_data = [
            {
                "id": 1,
                "name": "Concert in the Park",
                "start_time": "2024-10-02T10:00:00",
                "duration": 180,
                "location": "City Park",
                "image_url": "/media/concert_image.jpg",
                "registration_link": "http://register-concert.com",
                "short_description": "A live concert in the city park.",
                "long_description": "Enjoy a live concert featuring local bands in the beautiful setting of City Park.",
                "tags": [{"id": 1, "name": "Music"}, {"id": 2, "name": "Live"}],
            }
        ]
        
    def tearDown(self):
        cache.clear()

    @requests_mock.Mocker()
    def test_index_view_fetches_data_from_api(self, mocker):
        mocker.get(self.api_url, json=self.events_data)

        response = self.client.get(reverse("index", args=[2024, 10]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Concert in the Park")

class EventViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.api_url = "https://rekrutacja.teamwsuws.pl/events/1/"
        self.event_data = {
            "id": 1,
            "name": "Concert in the Park",
            "start_time": "2024-10-02T10:00:00",
            "duration": 180,
            "location": "City Park",
            "image_url": "/media/concert_image.jpg",
            "registration_link": "http://register-concert.com",
            "short_description": "A live concert in the city park.",
            "long_description": "Enjoy a live concert featuring local bands in the beautiful setting of City Park.",
            "tags": [{"id": 1, "name": "Music"}, {"id": 2, "name": "Live"}],
        }

    def tearDown(self):
        cache.clear()

    @requests_mock.Mocker()
    def test_event_view_fetches_data_from_api(self, mocker):
        mocker.get(self.api_url, json=self.event_data)
        response = self.client.get(reverse("event", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Concert in the Park")

        cached_event = cache.get("event-1")
        self.assertIsNotNone(cached_event)
        self.assertEqual(cached_event["name"], "Concert in the Park")

class SearchViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_search_view_returns_results(self):
        response = self.client.post(reverse("search"), {"search": "uws"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dyktando Siedleckie")