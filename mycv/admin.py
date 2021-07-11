from django.contrib import admin
from .models import *

# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    list_display= ('profile_img', 'name','city','phone','gmail','description', 'linkedinlink','githublink','twitterlink','facebooklink','fiverlink','cv_upload')
    
class ExpAdmin(admin.ModelAdmin):
    list_display=('designation','organization_name','description','start_date','end_date')

class EduAdmin(admin.ModelAdmin):
    list_display=('instituate_name','degree_name','course_name','start_date','end_date')

class SkillAdmin(admin.ModelAdmin):
    list_display=('skill_name','skill_percent')
    
class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','subject','message')
    
class ProjectAdmin(admin.ModelAdmin):
    list_display=('project_name','project_description','project_link','project_video')
    
    
# class IntAdmin(admin.ModelAdmin):
#     list_display=('description')
    
admin.site.register(About,AboutAdmin)
admin.site.register(Experience,ExpAdmin)
admin.site.register(Education,EduAdmin)
admin.site.register(Interest)
admin.site.register(Skill,SkillAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Project,ProjectAdmin)