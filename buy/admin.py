from django.contrib import admin
from .models import Listing, Comment, ListingImage
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Listing)
class BuyAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'author', 'created_on', 'status', 'manufacturer', 'likes', 'price', 'reserve', 'current_bid')
    search_fields = ['title']
    list_filter = ('manufacturer', 'likes', 'price')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)


@admin.register(ListingImage)
class ListingImageAdmin(admin.ModelAdmin):

    list_display = ['listing', 'image_preview']
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        from django.utils.html import format_html
        if obj.image:
            return format_html('<img src="{}" width="150" height="auto" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Image Preview'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('author', 'body_shortened', 'listing', 'created_on')
    search_fields = ('author__username', 'body', 'listing__title')
    list_filter = ('created_on', 'listing')

    def body_shortened(self, obj):
        return obj.body[:50]
    body_shortened.short_description = 'Comment'




