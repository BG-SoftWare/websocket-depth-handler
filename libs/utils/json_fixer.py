from decimal import Decimal

def my_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)

    # Далее можно описывать и другие свои типы, например MyFooFooBar
    # elif isinstance(obj, MyFooFooBar):
    #     return obj.get_super_foo_bar_value()

    # Если не удалось определить тип:
    return str(obj)