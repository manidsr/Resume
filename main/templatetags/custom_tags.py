from django import template

register = template.Library()

def GetResumeItem(value):
    return value.resumeitem_set.all()

register.filter('GetResumeItem', GetResumeItem)