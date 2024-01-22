from django import template
register = template.Library()

@register.simple_tag(name="getstatus")
def getstatus(status):
    ststus_list = [
        'Order Confirmed',
        'Order Processed',
        'Order Delivered',
        'Order Rejected'
    ]

    return ststus_list[status-1]