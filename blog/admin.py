from django.contrib import admin
from .models import (
    Article,
    IPAddress,
    Category,
    Comment,
    Like,
    SaveArticle
)

# Register your models here.


# IPAddress model admin
class IPAddressAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


# Category model admin
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


# Category inline
class CategoryInline(admin.TabularInline):
    model = Article.categories.through


# Article model admin
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline
    ]
    fieldsets = (
        ('اطلاعات مقاله', {
         'fields': ('title', 'description', 'image', 'author')}),
        ('بازدید و انتشار', {'fields': ('hits', 'publish_time')})
    )
    list_display = ('title', 'get_thumbnail',
                    'publish_time', 'created', 'updated')
    list_filter = ('publish_time', 'created')

    def get_queryset(self, request):
        qs = super(ArticleAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)


# Comment model Admin
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    def get_queryset(self, request):
        qs = super(CommentAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(article__author=request.user)


class LikeAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_filter = ('created',)

    def has_change_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        like_qs = super(LikeAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return like_qs
        return like_qs.filter(article__author=request.user)


# SaveArticle model Admin
class SaveArticleAdmin(admin.ModelAdmin):
    readonly_fields = ['created']

    def get_queryset(self, request):
        qs = super(SaveArticleAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(article__user=request.user)


admin.site.register(IPAddress, IPAddressAdmin)  # registering IPAddress model
admin.site.register(Category, CategoryAdmin)  # registering Category model
admin.site.register(Article, ArticleAdmin)  # registering Article model
admin.site.register(Comment, CommentAdmin)  # registering Comment model
admin.site.register(Like, LikeAdmin)  # registering Like model
admin.site.register(SaveArticle, SaveArticleAdmin)  # registering SaveArticle model
