# -*- coding: utf-8 -*-


# def make_shirt(t_type="L", content="I love Python"):
#     print("type=" + t_type + ": " + content)
#
#
# make_shirt()
# make_shirt("M")
# make_shirt(content="I love you")
#
#
# def greet_user(names):
#     """向列表中的每位用户发出简单的问候"""
#     for name in names:
#         msg = "Hello, " + name.title() + "!"
#         print(msg)
#
#
# usernames = ['hannah', 'ty', 'margot']
# greet_user(usernames)


# def make_pizza(*toppings):
#     print("\nMaking a pizza with the following toppings: ")
#     for topping in toppings:
#         print("- " + topping)
#
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


# def make_pizza(size, *toppings):
#     print("\nMaking a " + str(size) +
#           "-inch pizza with the folloing toppings:")
#     for topping in toppings:
#         print("- " + topping)
#
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


def build_profile(first, last, **user_info):
    profile = dict()
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton', field='physics')
print(user_profile)
