# # User Story #1! 

# #-----------Lists:

# #destinations
# destinations = ['Alabama', 'Vietnam', 'Washington D.C.', 'Monument Valley', 'Georgia'] 

# #restaurant
# restaurants = ["Mama's Kitchen", 'Bubba-Gump Shrimp', 'Buffet', 'Barbeque', 'Vietnamese Restaurant'] 

# #transportation
# getting_around_by = ['Bus', 'Walk', 'Helicopter', 'Car', 'Magic Shoes']

# #entertainment
# entertainment = ['Political Rally', 'Helicopter Ride', 'Cross-country hiking', 'Check out downtown', 'Boat ride', 'Party with some hippies']

# #----------- Random reselect:
# import random


# #----------- Confirm trip is complete:

# #----------- display completed trip:

import random

welcome_message = 'Hi and welcome to Gumpcations! A new and super popular tool for planning your Forrest Gump themed vacation!'
next_1 = "Next let's see how you'll be getting around."
#next_2 = str(f'If you are in {destination_result}, I imagine you are getting hungry.')


list_destinations = ['Alabama', 'Vietnam', 'Washington D.C.', 'Monument Valley', 'Georgia'] 

list_get_around = ['Bus', 'Helicopter', 'Car', 'Magic Shoes']

list_restaurants = ["Mama's Kitchen", 'a Bubba-Gump Shrimp diner', 'a Buffet', 'a Barbeque', 'a Vietnamese Restaurant'] 

list_entertainment = ['political rally', 'helicopter ride', 'Cross-country hiking', 'Check out downtown', 'Boat ride', 'Party with some hippies']



def user_name():
  input_name = input("First off, what's your first name?: ")
  print(f'Welcome, {input_name}!')
  return(input_name)

# def jenny_question():
#   response = input('May I call you Jenny? (Yes/No): ')
#   if response == 'Yes':
#     print("Great! That's my favorite name.")
#     return()
#   else:
#     print(f'No problem! {input_name} it is.')
  
# def is_jenny(answer):
#   response = input('May I call you Jenny? (Yes/No): ')
#   while response == 'Yes':
#     if response == 'Jenny':
#       print("Great! That's my favorite name.")
#       return(True)
#     else:
#       print(f'No problem! {input_name} it is.')

def begin_app():
  user_ready = input("Are you ready to see what's in your vacation's box of chocolates? (Type Yes or No): ")
  if user_ready == 'Yes':
    print("Great! First, let's pick your destination.")
    return
  else:
    print("Well come back when you're ready for a Gumpcation!")


def rand_destination(list):
  result = random.choice(list)
  print(f"Pack your suitcase and Curious George book, you're going to {result}!")
  return(result)


def rand_mode_of_transport(list):
  result = random.choice(list)
  print(f'How about that {guest}, you will be getting around {destination_result} by {result}!')
  return(result)


def rand_restaurant():
  result = random.choice(list_restaurants)
  print(f'Feeling hungry? Wait no longer! You will be eating dinner at {result}. Right on!')
  return(result)


def rand_entertainment():
  result = random.choice(list_entertainment)
  print(f"Finally, let's go have some fun! Your evening's entertainment will be {result}")
  return (result)


def wrap_up():
  print(f"Well, {guest}. So far, you'll be going to {destination_result}, you'll get around by {transport_result}, you'll be eating at {restaurant_result}, and for fun you'll {entertainment_result}. Awesome!")
  # change redo to give them the option to get new random selections
  input_confirm = input('Do you want to make any changes to your trip? (Yes or No): ')
  if input_confirm == "Yes" or "yes":
    make_final_selection()
  else: 
    print(f" Great! Have a nice trip!")

  # guest_decision = input('Please type "Confirm" to solidify your plans. Otherwise type "Redo" to start over again')
  # if guest_decision == 'Confirm' or 'confirm':
  #   return
  # elif guest_decision == 'redo' or 'Redo':
  #   make_final_selection(destination_result, transort_result, restaurant_result, entertainment_result, guest )

# def make_final_selection(destination, transportation, restaurant, entertainment, name):
  
  # while loop
  # with nexted if else statment to create a menu
  # Enter "1" to get a new destination
  # Enter "2" to get a new transportaion
  # Enter "3" for restaurant
  # Enter "4" for entertainment
  # Enter "5" to confirm your trip!
  # if user selecton = 1:
  #    destination = rand_destination()
 

#----The functions

print(welcome_message)
guest = user_name()
# is_jenny(answer)   #True
begin_app()
destination_result = rand_destination(list_destinations)
print(next_1)
transport_result = rand_mode_of_transport(list_get_around)
restaurant_result = rand_restaurant()
entertainment_result = rand_entertainment()
wrap_up()

