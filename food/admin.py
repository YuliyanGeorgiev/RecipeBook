from django.contrib import admin
from .models import Post
from .models import Choice
from .models import Comment

admin.site.register(Post)
admin.site.register(Choice)
admin.site.register(Comment)
