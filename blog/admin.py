from django.contrib import admin
from blog.models import  Post  , Category
from django_summernote.admin import SummernoteModelAdmin
from blog.models import Comment
# Register your models here.
# @admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    # fields = ('title' ,) 
    # exclude = 'title'
    list_display = ('title' ,'author' ,  'counted_view' , 'status' , 'published_date' , 'created_date' ,'author' )
    list_filter = ('status' , )
    ordering = ['-created_date']
    search_fields = ['title' , 'content']
    summernote_fields = ('content',)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    # fields = ('title' ,) 
    # exclude = 'title'
    list_display = ('name' ,'post' ,'approved','created_date' )
    # list_filter = ('status' , )
    ordering = ['-created_date']
    search_fields = ['post','approved']
    summernote_fields = ('name','post')
admin.site.register(Comment , CommentAdmin)
admin.site.register(Category)
admin.site.register(Post , PostAdmin)
