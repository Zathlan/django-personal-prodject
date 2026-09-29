from django.db import models
from django.urls import reverse

class Post(models.Model):
    item = models.CharField(max_length=200)
    owner = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=19, decimal_places=2)
    cover = models.ImageField(upload_to="images/", null=True, blank=True) 

    def __str__(self):
        return self.item

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
