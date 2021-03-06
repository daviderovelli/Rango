from django.contrib import admin
from Rango.models import Category,Page, UserProfile

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

#Display these columns in admin.py/categories
class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category','url')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
