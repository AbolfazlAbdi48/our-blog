from django.contrib import admin
from .models import (
    Article,
    IPAddress,
    Category
)

# Register your models here.


# IPAddress model admin
class IPAddressAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


# category model admin
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


# category inline
class CategoryInline(admin.TabularInline):
    model = Article.categories.through


# article model admin
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline
    ]
    fieldsets = (
        ('اطلاعات مقاله', {'fields': ('title', 'description', 'image', 'author')}),
        ('بازدید و انتشار', {'fields': ('hits', 'publish_time')})
    )
    list_display  = ('title', 'get_thumbnail', 'publish_time', 'created', 'updated')
    list_filter = ('publish_time', 'created')

    def get_queryset(self, request):
        qs = super(ArticleAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)


admin.site.register(IPAddress, IPAddressAdmin)  # registering IPAddress model
admin.site.register(Category, CategoryAdmin)  # registering Category model
admin.site.register(Article, ArticleAdmin)  # registering Article model
