from django.contrib import admin
# 和models同级目录
from .models import Topic, Entry

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)