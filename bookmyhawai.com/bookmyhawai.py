from show_flights import show_flights

available_data = ['jaipur', 'mumbai']

print('\n\t\t\tWelcome to BookmyHawai.com\n\n')

def check_flight():
    """check flight"""
    fromm = input('From: ').strip()
    if fromm not in available_data:
        print('Data not available.')
        return False
    too = input('To: ').strip()
    if too not in available_data:
        print('Data not available.')
        return False
    prompt_price = True
    while prompt_price:
        try:
            price_range = int(input('Enter price Range($5000 to ): '))
        except:
            pass
        else:
            if price_range <= 5000:
                print('Min price is $5000!')
                prompt_price = True
            else: 
                prompt_price = False
    show_flights(fromm, too, price_range)
    return True
        



while not check_flight():
    print('Try Again!\n')