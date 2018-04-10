# -*- coding: utf-8 -*-

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program:"
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)
#
# prompt = "\nPlease enter the name of a city you have visited: "
# prompt += "\n(Enter 'quit' when you are finished。）"

# while True:
#     city = input(prompt)
#
#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to " + city.title() + "!")

# responses = {}
# while True:
#     repeat = input("\nWould you like to respond (yes/no) ?")
#     if repeat == 'no':
#         break
#     name = input("\nWhat is your name?")
#     response = input("\nWhich mountain would you like to climb someday? ")
#     responses[name] = response
#
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(name + " would like to climb " + response)

sandwich_orders = ["sandwicha", "sandwichb", "sandwichc"]
finished_sandwiches = []

while sandwich_orders:
    curr_order = sandwich_orders.pop()
    print("I made your tuna sandwich" + curr_order)
    finished_sandwiches.append(curr_order)

print("finished sandwicher are:")

for sandwich in finished_sandwiches:
    print("\t" + sandwich)
