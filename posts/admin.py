from django.contrib import admin
from .models import Post

# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    # 레코드 개별 화면에서 확인용
    readonly_fields = ('id','content')
    # 리스트에서 표시할 컬럼
    list_display = ('id', 'content')
    # 리스트에서 clickable 할 속성
    list_display_links = ('id', 'content')
    
admin.site.register(Post, PostModelAdmin)