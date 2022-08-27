from .models import News
from django.contrib import admin


admin.site.register(News)


# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#
#     list_display = (
#         'title',
#         'is_publishable',
#         'created_at',
#         'updated_at',
#     )
#     list_filter = (
#         'is_publishable',
#         'created_at',
#         'updated_at',
#     )

# @admin.register(News)
# class MyModelAdmin(admin.ModelAdmin):
#     list_display = ['tag_list']
#
#     def get_queryset(self, request):
#         return super().get_queryset(request).prefetch_related('tags')
#
#     def tag_list(self, obj):
#         return u", ".join(o.name for o in obj.tags.all())
