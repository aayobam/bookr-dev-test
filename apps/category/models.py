from uuid import uuid4
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from="name")


    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"id": self.id})
    
