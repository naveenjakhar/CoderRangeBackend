from django.contrib import admin
from trainer.models import *
# Register your models here.
# admin.site.register(Trainer_profile)
# admin.site.register(Course_details)
class TrainercourseAdmin(admin.ModelAdmin):
    # search_fields = ['email']
    # list_display=('id','username','is_admin')
    list_display=('trainerId','coaching_courseid','countOfStudent','time')
    list_per_page = 10
admin.site.register(Trainercourse,TrainercourseAdmin)
# admin.site.register(Trainercourse)
admin.site.register(Coursedetails)
admin.site.register(discussion)
admin.site.register(Class_Review)