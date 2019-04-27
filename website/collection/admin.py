from django.contrib import admin
from .models import user_basic_detail, user_extra_detail, working_detail


class user_basic_admin(admin.ModelAdmin):
    list_display = ('id','user_id','username','name','address','intro','timestamp')
    class Meta:
        model = user_basic_detail

class user_extra_admin(admin.ModelAdmin):
    list_display = ('user_id','username','dob','gender','website_link','relationship_status','profession')
    class Meta:
        model = user_basic_detail

class working_detail_admin(admin.ModelAdmin):
    list_display = ('username','work_id','workplace')
    class Meta:
        model = working_detail


admin.site.register(user_basic_detail, user_basic_admin)
admin.site.register(user_extra_detail, user_extra_admin)
admin.site.register(working_detail, working_detail_admin)
