from django.contrib import admin
from .models import BookInfo,HeroInfo

class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 2

class BookInfoAdmin(admin.ModelAdmin):
    inlines = [HeroInfoInline]

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)