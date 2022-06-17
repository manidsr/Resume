from django.urls import path
from . import views

urlpatterns = [
    path("",views.IdentitiyFunc,name="IdentitiyFunc"),
    path("identitiy/",views.IdentitiyFunc,name="IdentitiyFunc"),
    path("skills/",views.SkillsFunc ,name="SkillsFunc"),
    path("services/",views.ServicesFunc ,name="ServicesFunc"),
    path("links/",views.LinksFunc,name="LinksFunc"),
    path("facts/",views.FactsFunc,name="FactsFunc"),
    path("animatedtext/",views.AnimatedTextFunc,name="AnimatedTextFunc"),
    path("resume/",views.ResumeFun,name="ResumeFun"),
    path("resume/<int:id>/",views.ResumeItemFun,name="ResumeItemFun"),
    path("portfilo/",views.PortfiloFun,name="PortfiloFun"),
    path("portfilo/<int:id>/",views.PortfiloItemFun,name="PortfiloItemFun"),
    path("partner/",views.PartnerFun,name="PartnerFun"),
    path("partner/<int:id>",views.PartnerInfo,name="PartnerInfo"),
    path("filters/",views.Filters,name="Filters"),
    path("settings/",views.SettingsFun,name="SettingsFun"),
]