from django.contrib import admin
from bookmark.models import Bookmark

# Register your models here.
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')

# 위에 데코레이터를 사용하지 않고 register 함수를 사용해서도 가능하다.
# admin.site.register(Bookmark, BookmarkAdmin)