from django.shortcuts import render
from Manager.models import Identitiy,Facts,SkillList,Services,Animatedtext,Link,Partner,Portfilo,Resume,Settings
from django.views.decorators.clickjacking import xframe_options_exempt
# Create your views here.

@xframe_options_exempt
def LightboxProject(response,id):

    portfilo = Portfilo.objects.first()
    portfiloProjects = portfilo.portfiloproject_set.get(id=id)
    
    return render(response,"main/portfolio-details.html",{"portfiloProjects":portfiloProjects})

def index(response):
    toPass = {}

    identitiy = Identitiy.objects.first()
    toPass["identitiy"] = identitiy

    fact = Facts.objects.first()
    toPass["fact"] = fact
    facts = fact.fact_set.all()
    toPass["facts"] = facts

    skill = SkillList.objects.first()
    toPass["skill"] = skill
    skills = skill.skill_set.all()
    toPass["skills"] = skills

    service = Services.objects.first()
    toPass["service"] = service
    services = service.service_set.all()
    toPass["services"] = services

    animatedtext = Animatedtext.objects.first()
    toPass["animatedtext"] = animatedtext

    links = Link.objects.all()
    toPass["links"] = links

    partners = Partner.objects.all()
    toPass["partners"] = partners

    portfilo = Portfilo.objects.first()
    toPass["portfilo"] = portfilo
    portfiloFilters = portfilo.portfilofilter_set.all()
    toPass["portfiloFilters"] = portfiloFilters
    portfiloProjects = portfilo.portfiloproject_set.all()
    toPass["portfiloProjects"] = portfiloProjects

    toPass["resume"] = Resume.objects.all()

    toPass["setting"] = Settings.objects.first()

    return render(response,"main/index.html",toPass)