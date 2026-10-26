from django import template

register = template.Library()


@register.filter
def priority_label(value):
    if value == "high":
        return "High Priority"
    elif value == "medium":
        return "Medium Priority"
    elif value == "low":
        return "Low Priority"

    return value