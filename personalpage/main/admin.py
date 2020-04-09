from django.contrib import admin
from .models import Personal, Links, Education, Languages, Interests, CareerProfile, Experiences, Projects, Skills
# Register your models here.

@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ('name' , 'role')

@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    pass

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree' , 'university' , 'years')

@admin.register(Languages)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('language',)

@admin.register(Interests)
class InterestsAdmin(admin.ModelAdmin):
    list_display = ('interest',)

@admin.register(CareerProfile)
class CareerProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Experiences)
class ExperiencesAdmin(admin.ModelAdmin):
    list_display = ('title', 'company' , 'years')

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('name', 'percent')