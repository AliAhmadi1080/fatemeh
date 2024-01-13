from django.contrib import admin
from .models import *

class AdminBlog(admin.ModelAdmin):
    list_display=('id','titel','date','author','like_count')
    list_filter=('author','titel')
    list_display_links=('id',)
    readonly_fields = ('date','like_count')
    
    fieldsets = [
        (
            ('اطلاعات'),
            {
                "fields": ['titel','author'],
            },
            
        ),
        (
            ('بدنه'),
            {
                'fields':['sub_titel','categorys','text']
            }
        ),
        (
            ('کاربر'),
            {
                'fields':['like_count','date']
            }
        ),
    ]

    add_fieldsets = (
            (
                ('اطلاعات'),
                {
                    "fields": ['titel','author'],
                },
            ),
            (
                ('بدنه'),
                {
                    'fields': ['sub_titel','categorys','text']
                }
            ),
        )
    
    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)

    

admin.site.register(Blog,AdminBlog)
admin.site.register(Categorys)
admin.site.register(Comment)
admin.site.register(Like)
