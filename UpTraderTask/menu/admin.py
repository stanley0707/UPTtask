from django.contrib import admin
from menu.models import Menu, Post, Option
from mptt.admin import MPTTModelAdmin

class MenuAdminInline(admin.TabularInline):
    model = Menu
    extra = 1
    
    prepopulated_fields = {
        'slug': ('name',),
    }

class MenuAdmin(MPTTModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }

    inlines = [MenuAdminInline]

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',),
    }

class OptionAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Menu, MenuAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Option, OptionAdmin)
