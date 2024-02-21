from django.contrib import admin
from .models import Listing, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Listing)
class BuyAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'author' ,'created_on', 'status','manufacturer', 'likes', 'price')
    search_fields = ['title']
    list_filter = ('manufacturer', 'likes', 'price')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)

# Register your models here.
admin.site.register(Comment)


