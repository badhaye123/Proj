from django.contrib import admin
from .models import ApprovalRequest, Requester, Approver
from django.contrib.auth.models import User
# # Register your models here.



class UserAdmin(admin.ModelAdmin):
    list_display = ('is_approver','is_requester')
admin.site.register(User,UserAdmin)


class RequesterAdmin(admin.ModelAdmin):
    list_display = ('user','name','age')

admin.site.register(Requester,RequesterAdmin)

class ApproverAdmin(admin.ModelAdmin):
    list_display = ('user','name','age')

admin.site.register(Approver,RequesterAdmin)



class ApprovalRequestAdmin(admin.ModelAdmin):
    list_display = ('id','type', 'assigned_to', 'date_of_deployment', 'commit_id', 'branch', 'deployed_environment', 'changes','status','timestamp')
    
admin.site.register(ApprovalRequest,ApprovalRequestAdmin)