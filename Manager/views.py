from distutils.log import info
from tkinter import Image
from django import http
from django.shortcuts import HttpResponseRedirect, render,HttpResponse
from .models import Identitiy,Link,Animatedtext,SkillList,Facts,Services,Partner,Resume,Portfilo,Settings
# Create your views here.

def Filters(response):
    filters = Portfilo.objects.first().portfilofilter_set.all()

    if response.method == "POST":
        if response.POST.get("add"):
            newFilter = Portfilo.objects.first().portfilofilter_set.create(name="")
            newFilter.save()
        if response.POST.get("change"):
            idFilter = response.POST.get("id")
            toChange = Portfilo.objects.first().portfilofilter_set.get(id=idFilter)
            toChange.name = response.POST.get("name")
            toChange.save()
        if response.POST.get("delete"):
            idFilter = response.POST.get("id")
            toDelete = Portfilo.objects.first().portfilofilter_set.get(id=idFilter)
            toDelete.delete()
        return HttpResponseRedirect("/Manager/filters")
    return render(response,"Manager/Filters.html",{"filters":filters})

def SettingsFun(response):
    settings = Settings.objects.first()

    if response.method == "POST":
        if response.POST.get("save"):
            settings.blockHero = response.POST.get("blockHero") == "on"
            settings.blockAbout = response.POST.get("blockAbout") == "on"
            settings.blockFacts = response.POST.get("blockFacts") == "on"
            settings.blockSkills = response.POST.get("blockSkills") == "on"
            settings.blockResume = response.POST.get("blockResume") == "on"
            settings.blockPortfilo = response.POST.get("blockPortfilo") == "on"
            settings.blockServices = response.POST.get("blockServices") == "on"
            settings.blockPartners = response.POST.get("blockPartners") == "on"
            settings.blockContact = response.POST.get("blockContact") == "on"
            settings.save()
        
        return HttpResponseRedirect("/Manager/settings")
    
    return render(response,"Manager/Settings.html",{"settings":settings})

def PortfiloItemFun(response,id):

    projects = Portfilo.objects.first()
    filters = Portfilo.objects.first().portfilofilter_set.all()
    project = projects.portfiloproject_set.get(id=id)

    if response.method == "POST":
        if response.POST.get("save"):
            project.projectTitle = response.POST.get("projectTitle")
            project.category = response.POST.get("category")
            project.projectDate = response.POST.get("projectDate")
            project.projectUrl = response.POST.get("projectUrl")
            project.company = response.POST.get("company")
            project.projectInfo = response.POST.get("projectInfo")
            project.portfiloFilter = response.POST.get("filter")
            if len(response.FILES) != 0:
                project.image = response.FILES['image']
            project.save()
            return HttpResponseRedirect("/Manager/portfilo/"+str(id))

    return render(response,"Manager/PortFiloItem.html",{"res":project,"filters":filters})

def PortfiloFun(response):

    if response.method == "POST":
        if response.POST.get("delete"):
            idProject = response.POST.get("id")
            toDelete = Portfilo.objects.first().portfiloproject_set.get(id=idProject)
            toDelete.delete()

        if response.POST.get("changeName"):
            idProject = response.POST.get("id")
            toChange = Portfilo.objects.first().portfiloproject_set.get(id=idProject)
            toChange.projectTitle = response.POST.get("title")
            toChange.save()
        
        if response.POST.get("add"):
            project = Portfilo.objects.first().portfiloproject_set.create(projectTitle="",category="",projectDate="",projectUrl="",company="",projectInfo="",portfiloFilter="",image="")
            project.save()

        return HttpResponseRedirect("/Manager/portfilo")

    toPass = {}

    toPass["projects"] = Portfilo.objects.first().portfiloproject_set.all()

    return render(response,"Manager/Portfilo.html",toPass)

def ResumeItemFun(response,id):
    resume = Resume.objects.get(id=id)
    resumeItem = resume.resumeitem_set.all()

    if response.method == "POST":
        if response.POST.get("save"):

            resumeId = response.POST.get("id")
            toSave = Resume.objects.get(id=id).resumeitem_set.get(id=resumeId)
            toSave.title = response.POST.get("title")
            toSave.time = response.POST.get("time")
            toSave.secondTitle = response.POST.get("secondTitle")
            toSave.info = response.POST.get("info")
            toSave.save()
        if response.POST.get("delete"):
            resumeId = response.POST.get("id")
            toDelete = Resume.objects.get(id=id).resumeitem_set.get(id=resumeId)
            toDelete.delete()
        if response.POST.get("add"):
            toAdd = Resume.objects.get(id=id).resumeitem_set.create(title="",time="",secondTitle="",info="")
            toAdd.save()
        
        return HttpResponseRedirect("/Manager/resume/"+str(id))

    return render(response,"Manager/ResumeItem.html",{"resume":resumeItem})

def ResumeFun(response):

    if response.method == "POST":
        if response.POST.get("delete"):
            idResume = response.POST.get("id")
            toDelete = Resume.objects.get(id=idResume)
            toDelete.delete()

        if response.POST.get("changeName"):
            idResume = response.POST.get("id")
            toChange = Resume.objects.get(id=idResume)
            toChange.title = response.POST.get("title")
            toChange.save()

        if response.POST.get("add"):
            resume = Resume.objects.create(title="")
            resume.save()

        return HttpResponseRedirect("/Manager/resume")

    toPass = {}

    toPass["resume"] = Resume.objects.all()

    return render(response,"Manager/Resume.html",toPass)

def PartnerInfo(response,id):
    
    partner = Partner.objects.get(id=id)

    if response.method == "POST":
        if response.POST.get("save"):
            idPartner = int(response.POST.get("id"))
            toSave = Partner.objects.get(id=idPartner)
            toSave.name = response.POST.get("name")
            toSave.job = response.POST.get("job")
            toSave.info = response.POST.get("info")
            if len(response.FILES) != 0:
                toSave.image = response.FILES['image']
            toSave.save()

            return HttpResponseRedirect("/Manager/partner/"+str(id))

    return render(response,"Manager/Partner.html",{"person":partner})

def PartnerFun(response):

    if response.method == "POST":
        if response.POST.get("changeName"):
            idPerson = response.POST.get("id")
            toSave = Partner.objects.get(id=idPerson)
            toSave.name = response.POST.get("name")
            if len(response.FILES) != 0:
                toSave.image = response.POST.get("image")
            toSave.save()
        if response.POST.get("delete"):
            idPerson = response.POST.get("id")
            toDelete = Partner.objects.get(id=idPerson)
            toDelete.delete()
        if response.POST.get("add"):
            newPerson = Partner.objects.create(name="",job="",info="",image="")
            newPerson.save()
        
        return HttpResponseRedirect("/Manager/partner")

    partner = Partner.objects.all()
    return render(response,"Manager/Partners.html",{"partner":partner})

def IdentitiyFunc(response):
    Id = Identitiy.objects.first()

    if  response.method == "POST":
        if response.POST.get("save"):
            Id.name = str(response.POST.get("name"))
            Id.age = int(response.POST.get("age"))
            Id.phoneNumber = str(response.POST.get("phoneNumber"))
            Id.title = str(response.POST.get("title"))
            Id.email = str(response.POST.get("email"))
            Id.city = str(response.POST.get("city"))
            Id.job = str(response.POST.get("job"))
            Id.degree = str(response.POST.get("degree"))
            Id.website = str(response.POST.get("website"))
            Id.info = str(response.POST.get("info"))
            if len(response.FILES) != 0:
                Id.image = response.FILES['image']
            Id.save()

        return HttpResponseRedirect("/Manager/identitiy")

    return render(response,"Manager/Identitiy.html",{"Id":Id})
    
def SkillsFunc(response):
    dbSkillList = SkillList.objects.first()
    dbSkills = dbSkillList.skill_set.all()

    if  response.method == "POST":
        if response.POST.get("add"):
            newSkill = dbSkillList.skill_set.create(name="",value=0)
            newSkill.save()
        if response.POST.get("save"):
            idSkill = int(response.POST.get("id"))
            toSave = dbSkillList.skill_set.get(id=idSkill)
            toSave.name = str(response.POST.get("name"))
            toSave.value = int(response.POST.get("value"))
            toSave.save()
        elif response.POST.get("delete"):
            idSkill = int(response.POST.get("id"))
            toDelete = dbSkillList.skill_set.get(id=idSkill)
            toDelete.delete()
           

        return HttpResponseRedirect("/Manager/skills")
            
    return render(response,"Manager/Skills.html",{"skills":dbSkills})

def ServicesFunc(response):
    dbServicesList = Services.objects.first()
    dbServices = dbServicesList.service_set.all()

    if  response.method == "POST":
        if response.POST.get("add"):
            newService = dbServicesList.service_set.create(name="",info="")
            newService.save()
        if response.POST.get("save"):
            idService = int(response.POST.get("id"))
            toSave = dbServicesList.service_set.get(id=idService)
            toSave.name = str(response.POST.get("name"))
            toSave.info = str(response.POST.get("info"))
            toSave.save()
        elif response.POST.get("delete"):
            idService = int(response.POST.get("id"))
            toDelete = dbServicesList.service_set.get(id=idService)
            toDelete.delete()
           

        return HttpResponseRedirect("/Manager/services")

    return render(response,"Manager/Services.html",{"services":dbServices})

def LinksFunc(response):
    links = Link.objects.all()

    if  response.method == "POST":
        if response.POST.get("add"):
            newLink = Link.objects.create(name="",link="")
            newLink.save()
        if response.POST.get("save"):
            idlink = int(response.POST.get("id"))
            DbLink = Link.objects.get(id=idlink)
            DbLink.name = str(response.POST.get("name"))
            DbLink.link = str(response.POST.get("link"))
            DbLink.save()
        elif response.POST.get("delete"):
            idlink = int(response.POST.get("id"))
            DbLink = Link.objects.get(id=idlink)
            DbLink.delete()
           

        return HttpResponseRedirect("/Manager/links")
            
            
    return render(response,"Manager/Links.html",{"links":links})

def FactsFunc(response):
    dbFactsList = Facts.objects.first()
    dbfacts = dbFactsList.fact_set.all()

    if  response.method == "POST":
        if response.POST.get("add"):
            newFact = dbFactsList.fact_set.create(name="",value=0)
            newFact.save()
        if response.POST.get("save"):
            idFact = int(response.POST.get("id"))
            toSave = dbFactsList.fact_set.get(id=idFact)
            toSave.name = str(response.POST.get("name"))
            toSave.value = int(response.POST.get("value"))
            toSave.save()
        elif response.POST.get("delete"):
            idFact = int(response.POST.get("id"))
            toDelete = dbFactsList.fact_set.get(id=idFact)
            toDelete.delete()
           

        return HttpResponseRedirect("/Manager/facts")
            
    return render(response,"Manager/Facts.html",{"facts":dbfacts})

def AnimatedTextFunc(response):
    animText = Animatedtext.objects.first()

    if response.method == "POST":
        if response.POST.get("save"):
            animText.beforeText = str(response.POST.get("beforeText"))
            animText.afterText = str(response.POST.get("afterText"))
            animText.animtedText = str(response.POST.get("animtedText"))
            animText.save()

        return HttpResponseRedirect("/Manager/animatedtext")

    return render(response,"Manager/AnimatedText.html",{"anim":animText})