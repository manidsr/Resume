from django.contrib import admin
from .models import Services,Service,Facts,Fact,Identitiy,SkillList,Skill,Animatedtext,Link,Partner,Portfilo,PortfiloProject,PortfiloFilter,Resume,ResumeItem,Settings
# Register your models here.

admin.site.register(Services)
admin.site.register(Service)
admin.site.register(Facts)
admin.site.register(Fact)
admin.site.register(Identitiy)
admin.site.register(SkillList)
admin.site.register(Skill)
admin.site.register(Link)
admin.site.register(Animatedtext)
admin.site.register(Partner)
admin.site.register(Portfilo)
admin.site.register(PortfiloProject)
admin.site.register(PortfiloFilter)
admin.site.register(Resume)
admin.site.register(ResumeItem)
admin.site.register(Settings)