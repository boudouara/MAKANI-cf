from django.contrib import admin
from mybasic_app.models import (ToDolist,Item,Chercheur
 ,Evaluateur ,User,Commite,Conferance,Topic,Article)




admin.site.register(ToDolist)
admin.site.register(Item)





class myFilterAdmin(admin.ModelAdmin):
    list_display = ('email','username' )  # displays the properties mentioned in the tuple
    list_filter = ('is_evaluteur','is_chercheur','is_superuser') 
    search_fields = ['email','username',]
    #prepopulated_fields = {'slug': ('title',)}





admin.site.register(Commite)

admin.site.register(Chercheur)
admin.site.register(Evaluateur)


admin.site.register(User,myFilterAdmin)


admin.site.register(Conferance)
admin.site.register(Topic)



admin.site.register(Article)
