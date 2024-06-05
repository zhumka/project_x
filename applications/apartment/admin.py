from django.contrib import admin
from applications.apartment.models import Comment, Apartment, Category, ApartmentAmenity


@admin.register(Apartment)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'like_count']
    list_filter = ['owner']
    search_fields = ['title']

    def like_count(self, obj):
        return obj.likes.filter(is_like=True).count()


@admin.register(ApartmentAmenity)
class ApartmentAmenityAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Category)
admin.site.register(Comment)
