from django import template

register = template.Library()


def _expand_obj__bad(obj, max_depth=5):
    """This is bad, ONLY use for debugging!"""
    if max_depth < 1:
        return obj
    max_depth -= 1

    if type(obj) in (tuple, list, int, str):
        return obj
    elif hasattr(obj, '__dict__'):
        return {k: _expand_obj__bad(v, max_depth=max_depth) for k, v in obj.__dict__.items()}


@register.filter
def debug(obj):
    return str(_expand_obj__bad(obj, max_depth=3))
