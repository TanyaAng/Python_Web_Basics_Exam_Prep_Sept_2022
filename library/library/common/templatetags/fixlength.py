from django import template

register = template.Library()


@register.filter
def fixed_items_in_row(items, fixed_length):
    length = len(list(items))
    result = []
    if length > fixed_length:
        for idx in range(0, length, fixed_length):
            result.append(items[idx:(idx + fixed_length)])
        return result

    return None
