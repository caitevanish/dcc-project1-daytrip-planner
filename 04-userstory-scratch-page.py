import random

#lists
list_destinations = ['Alabama', 'Vietnam', 'Washington D.C.', 'Monument Valley', 'Georgia'] 

list_get_around = ['Bus', 'Walk', 'Helicopter', 'Car', 'Magic Shoes']

list_restaurants = ["Mama's Kitchen", 'a Bubba-Gump Shrimp diner', 'a Buffet', 'a Barbeque', 'a Vietnamese Restaurant'] 

list_entertainment = ['political rally', 'helicopter ride', 'Cross-country hiking', 'Check out downtown', 'Boat ride', 'Party with some hippies']



print(random.choice(list_destinations))

def random_selector(list):
  result = random.choice(list)
  print(result)
  return result

selected_destination = random_selector(list_destinations)
selected_transportaion = random_selector(list_get_around)
random_selector(list_restaurants)
random_selector(list_entertainment)

def display_trip(destination, transportaion, restaurant, entertainment, guest):
  print(f"Well, {guest}. So far, you'll be going to {destination}, you'll get around by {transportaion}, you'll be eating at {restaurant}, and for fun you'll be {entertainment}. Awesome!")
  break

display_trip(selected_destination, selected_transportaion)