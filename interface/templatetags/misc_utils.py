import datetime
from django import template
import colorsys

register = template.Library()


def clamp(x):
    return int(max(0, min(x, 255)))


@register.simple_tag
def pastel_for_depth(i):
    # original settings: (h=i*63, s=0.33, v=0.8)
    r, g, b = colorsys.hsv_to_rgb(((i * 63) % 255) / 255.0, 0.33, 0.8)
    return "#{0:02x}{1:02x}{2:02x}".format(clamp(r * 255), clamp(g * 255), clamp(b * 255))


@register.filter(name='from_unix')
def from_unix(value):
    return datetime.datetime.fromtimestamp(int(value))