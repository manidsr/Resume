from django.db import models
# Create your models here.

class Settings(models.Model):
    blockHero = models.BooleanField(default=True)
    blockAbout = models.BooleanField(default=True)
    blockFacts = models.BooleanField(default=True)
    blockSkills = models.BooleanField(default=True)
    blockResume = models.BooleanField(default=True)
    blockPortfilo = models.BooleanField(default=True)
    blockServices = models.BooleanField(default=True)
    blockPartners = models.BooleanField(default=True)
    blockContact = models.BooleanField(default=True)

class Resume(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class ResumeItem(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    secondTitle = models.CharField(max_length=100)
    info = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Portfilo(models.Model):
    title = models.CharField(max_length=50)
    info = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class PortfiloProject(models.Model):
    portfilo = models.ForeignKey(Portfilo,on_delete=models.CASCADE,null=True,blank=True)
    projectTitle = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    projectDate = models.CharField(max_length=50)
    projectUrl = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    projectInfo = models.CharField(max_length=500)
    portfiloFilter = models.CharField(max_length=50)
    image = models.ImageField(null=True,blank=True,upload_to="images/")

    def __str__(self):
        return self.projectTitle

class PortfiloFilter(models.Model):
    portfilo = models.ForeignKey(Portfilo,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
        
class Partner(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    info = models.CharField(max_length=100)
    image = models.ImageField(null=True,blank=True,upload_to="images/")

    def __str__(self):
        return self.name

class Link(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField()

    def __str__(self):
        return self.name

class Animatedtext(models.Model):
    beforeText = models.CharField(max_length=50)
    afterText = models.CharField(max_length=50)
    animtedText = models.CharField(max_length=50)

    def __str__(self):
        return self.beforeText+" "+self.animtedText+" "+self.afterText
    
class Services(models.Model):
    name = models.CharField(max_length=50)
    info = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Service(models.Model):
    services = models.ForeignKey(Services,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Facts(models.Model):
    name = models.CharField(max_length=50)
    info = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Fact(models.Model):
    facts = models.ForeignKey(Facts,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.IntegerField()

    def __str__(self):
        return self.name

class Identitiy(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phoneNumber = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    brithDay = models.CharField(max_length=100)
    website = models.CharField(max_length=200)
    info = models.CharField(max_length=500)
    image = models.ImageField(null=True,blank=True,upload_to="images/")
    def __str__(self):
        return self.name

class SkillList(models.Model):
    name = models.CharField(max_length=200)
    info = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Skill(models.Model):
    skilllist = models.ForeignKey(SkillList,on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    value = models.IntegerField()

    def __str__(self):
        return self.name