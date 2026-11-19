from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Post
from decimal import Decimal

class PostTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="apple sauce", 
            password="SuperPowerAppleSauceMakesMeSuperStrong123123123"
        )
        self.post = Post.objects.create(
            item="apple sauce",
            owner=self.user,
            description="very yummy mmmmmmmmm",
            price=9999.99
        )

    def test_post_string_representation(self):
        self.assertEqual(str(self.post), "apple sauce")

    def test_get_absolute_url(self):
        self.assertEqual(
            self.post.get_absolute_url(), 
            reverse("post_detail", kwargs={"pk": self.post.pk})
        )

    def test_posts_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "apple sauce")

    def test_post_detail_view(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk": self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post_detail.html")
        self.assertContains(response, "very yummy mmmmmmmmm")

    def test_post_create_view(self):
        self.assertEqual(Post.objects.count(), 1)
        response = self.client.post(reverse("post_new"), data={
            "item": "qwertyuiopasdf",
            "owner": self.user.id,
            "description": "woahwoahwohawohaw",
            "price": 52321.11
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 2)

    def test_post_update_view(self):
        response = self.client.post(
            reverse("post_edit", kwargs={"pk": self.post.pk}), 
            data={
                "item": "mnbvcxzlkjhgfdsa",
                "owner": self.user.id,
                "description": "poiuytrewqasdfghjkl",
                "price": 22.22
            }
        )
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.item, "mnbvcxzlkjhgfdsa")
        self.assertEqual(self.post.price, Decimal("22.22")) 

    def test_post_delete_view(self):
        self.assertEqual(Post.objects.count(), 1)
        response = self.client.post(reverse("post_delete", kwargs={"pk": self.post.pk}))
        self.assertRedirects(response, reverse("home"))
        self.assertEqual(Post.objects.count(), 0)
