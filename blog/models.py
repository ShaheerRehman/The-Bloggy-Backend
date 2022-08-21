from django.utils.text import slugify

from users.models import New
from django.db import models
from django.utils import timezone



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=200)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published', unique=True, null=False)
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(New, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=15, choices=options, default='published')
    objects = models.Manager() # default manager
    postobjects = PostObjects() # custom manager

    class Meta:
        ordering = ('-published',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

