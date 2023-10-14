from decimal import Decimal


def my_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)

    # Now, you can describe another types, for example MyFooBar
    # elif isinstance(obj, MyFooFooBar):
    #     return obj.get_super_foo_bar_value()

    # If type is unknown:
    return str(obj)
