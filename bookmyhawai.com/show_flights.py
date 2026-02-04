import json

# get flights data from flights_info.json
with open('flights_info.json') as f:
    flights = json.load(f)


def show_flights(fromm, too, price_range):
    if fromm == 'jaipur' and too == 'mumbai':
        user_flights = flights['jaipur_to_mumbai']
    elif fromm == 'mumbai' and too == 'jaipur':
        user_flights = flights['mumbai_to_jaipur']
    
    for flight in user_flights:
        if flight['price_per_person'] <= price_range:
            # print a beutiful flights showing table
            print('\t------------------------------------------------------------------')
            print(f'\t| {flight['name']}\t| {flight['departure_time']}\t -{flight['stop']}-stop-\t {flight['arrival_time']}\t| ${flight['price_per_person']} \t|')
            print('\t------------------------------------------------------------------')