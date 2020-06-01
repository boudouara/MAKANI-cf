from django.contrib import admin
from Contact_Info_Adminstration.models import Contact_MAKANI_CF,SearchQuery


# Customize the way the admin panel looks
class PostAdmin(admin.ModelAdmin):
    list_display = ('title_de_problem', 'slug', 'status', 'created_on')  # displays the properties mentioned in the tuple
    list_filter = ('created_on',) 
    search_fields = ['title_de_problem', 'content']
    prepopulated_fields = {'slug': ('title_de_problem',)}



# Register your models here.
admin.site.register(Contact_MAKANI_CF, PostAdmin)



admin.site.register(SearchQuery)