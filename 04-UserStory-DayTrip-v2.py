# # User Story #1 - Day Trip planner - 'Gumpcations' - VERSION 2

import random
import sys

# Lists

list_destinations = ['Alabama', 'Vietnam', 'Washington D.C.', 'Monument Valley', 'Georgia', 'China'] 

list_get_around = ['Bus', 'Helicopter', 'Car', 'your Magic Shoes', 'a Volkswagon bus']

list_restaurants = ["Mama's Kitchen", 'a Bubba-Gump Shrimp diner', 'a Buffet', 'a Barbeque', 'a Vietnamese Restaurant'] 

list_entertainment = ['political rally', 'a helicopter ride', 'Cross-country hiking', 'play ping-pong', 'a Boat ride', 'Party with some hippies']

# Functions

def TripPlanner_Welcome():
  input_name = input("Hi and welcome to Gumpcations! A new and super popular tool for planning your Forrest Gump themed day-trip! What's your first name?: ")
  print(f'Welcome, {input_name}!')
  return(input_name)

def jenny_question(input_name):
  jenny_answer = input('May I call you, Jenny? (Y/N): ')
  if jenny_answer == 'Y':
    input_name = "Jenny"
    print("Great! Jenny is my favorite name.")
    return input_name    
  elif jenny_answer == 'N':  
    print(f'Alright, {input_name} it is.')
    return input_name

def begin_app():
  user_ready = input("Are you ready to see what's in your vacation's box of chocolates? (Y/N): ")
  if user_ready == 'Y':
      print("Great! First, let's pick your destination.")
      return True
  else:
      print("Well come back when you're ready for a Gumpcation!")
      sys.exit()

def random_selector_main(list_name):
  result = random.choice(list_name)
  if list_name == list_destinations:
   print(f"Pack your suitcase and Curious George book, you're going to {result}!")
   return(result)

  elif list_name == list_get_around:
    print(f'How about that, {user_name}, you will be getting around {selected_destination} by {result}!')
    return(result)

  elif list_name == list_restaurants:
    print(f'Feeling hungry? Wait no longer! You will be eating dinner at {result}. Right on!')
    return(result)   

  elif list_name == list_entertainment:
    print(f"Finally, let's go have some fun! Your evening's entertainment will be {result}")
    return (result)

# def final_selector(selected_item):
#   answer = input("Are you happy with this selection? Y/N: ")
#   while answer != "Y":
#     if answer == "Y":
#       print('Great!')
#       return 
#     else:
#       print("No problem! Let's give it another go...")
#       # if selec
#       random_selector_edit()


# --------------------------------- finalizing plans

def final_tripPlans(destination, transportation, restaurant, entertainment):
  print(f"Well, {user_name}. So far, you'll be going to {destination}, you'll get around by {transportation}, you'll be eating at {restaurant}, and for fun you'll {entertainment}. Groovy!")
  
  change_answer = input('Do you want to make any changes to your trip? Y/N: ')
  if change_answer == "N":
    print(f'Wonderful! Have a great time, {user_name}, and thank YOU for using Gumpcations!')
    return
  else:
    change_item()



def change_item():
  edit_item = input("If you want to change your destination, press '1'. For mode of transportation, type '2'. For restaurant, type '3'. For entertainment, type '4': ")
  
  if edit_item == "1":
    destination = random_destination_edit(list_destinations)
    return(destination)

  if edit_item == "2":
    random_transport_edit(list_get_around)
    return 

  # if edit_item == "3":
  #   random_selector_edit(list_restaurants)
  #   return
  
  # if edit_item == "4":
  #   random_selector_edit(list_entertainment)
  #   return
  
  else:
    final_tripPlans()



# def random_selector_edit(list_name):
#   result = random.choice(list_name)

#   if list_name == list_destinations:
#    result = input(f"Would you like to go to {result}? Y/N: ")
#    if result == "Y":
#      return(result)

#     elif result == "N":
#     random_selector_edit(list_destinations)

def random_destination_edit(final_destination):
  edit_destination = random.choice(list_destinations)
  result = input(f"Would you like to go to {edit_destination}? Y/N: ")
  while result != "Y":
    random_destination_edit(list_destinations) 
  if result == "Y":
    edit_destination = final_destination
    return(final_destination)
  else:
    return

def random_transport_edit(final_transport):
  edit_transport = random.choice(list_get_around)
  result = input(f"Would you like to go to by {edit_transport}? Y/N: ")
  while result != "Y":
    random_destination_edit(list_get_around) 
  if result == "Y":
    edit_transport = final_transport
    return(final_transport)

    
    

input_name = TripPlanner_Welcome()
user_name = jenny_question(input_name)
is_ready = begin_app()
selected_destination = random_selector_main(list_destinations)
# final_selector(selected_destination)
selected_transportation = random_selector_main(list_get_around)
# final_selector(selected_destination)
selected_restaurant = random_selector_main(list_restaurants)
selected_entertainment = random_selector_main(list_entertainment)
final_tripPlans(selected_destination, selected_transportation, selected_restaurant, selected_entertainment)
