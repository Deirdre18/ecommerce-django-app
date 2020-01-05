# to make sure posts are accessible from backend.

from django.contrib import admin
from .models import Post

admin.site.register(Post)
