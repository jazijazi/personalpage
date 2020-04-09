from django.shortcuts import render
from django.http import HttpResponse
from .models import Personal, Links, Education, Languages, Interests, CareerProfile, Experiences, Projects, Skills
def index(request):
    personal = Personal.objects.all().last()
    links = Links.objects.all().last()
    educations = Education.objects.all()
    languages = Languages.objects.all()
    interests = Interests.objects.all()
    careerProfile = CareerProfile.objects.all().last()
    experiences = Experiences.objects.all()
    projects = Projects.objects.all()
    skills = Skills.objects.all()

    context = {'personal': personal ,
                'links':links ,
                'educations':educations ,
                'languages':languages ,
                'interests':interests ,
                'careerProfile':careerProfile ,
                'experiences':experiences ,
                'projects':projects ,
                'skills':skills,
            }

    return render (request , 'main/index.html' , context)
    #