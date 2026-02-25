from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'time_period',
    )

    search_fields = (
        'title',
        'description',
        'learning',
    )

    ordering = ('title',)

    fieldsets = (
        ('Blog Information', {
            'fields': ('title', 'description', 'learning')
        }),
        ('Certification Details', {
            'fields': ('time_period', 'certificate_image'),
            'description': 'Fill this section only if this blog is about a certification'
        }),
    )
