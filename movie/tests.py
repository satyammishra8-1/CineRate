from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.apps import apps


class CineRateSmokeTests(TestCase):
    def setUp(self):
        Movie = apps.get_model("movie", "Movie")
        User = get_user_model()
        self.movie = Movie.objects.create(
            title="With Love",
            description="A slice-of-life romantic drama.",
            genre="Romantic Drama",
            release_date="2026-02-06",
        )
        self.normal_user = User.objects.create_user(
            username="viewer1",
            password="StrongPassword123!"
        )

    def test_home_page_loads_with_movies(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "With Love")

    def test_login_page_loads(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)