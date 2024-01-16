# COSTCO PARKING LOT CART MANAGEMENT MODEL 

#libraries:
import time 
import random 

# PART 1: MODEL SET UP 
'''
FUNCTION 1.a: PARAMETERS 
Parameter retrieval function: ask the user the following questions:
1. How many cart pushers are working ? 
2. How busy is the warehouse (on a scale of 0 to 10) ? 
'''

def model_init(): 
    print('Welcome to the Costco Warehouse #97 Parking Lot.') #welcome the user 
    
    qty_cart_pushers = input('How many cart pushers are working (0 - 6) ?    ')
    busy_rating = input('How busy is the warehouse (0 - 10) ?    ')

    return qty_cart_pushers, busy_rating

'''
FUNCTION 1.b: CREATE CORRALS
There are 22 corrals on site, each with a capacity of 24 carts (before considered overflowing)
There is 1 pad, which has a initial number of carts of 24 * 4 = 96
'''
def lot_builder(): 
    pad = [] # var pad is a list 
    corrals = {} # var corrals is a dictionary of lists 
    
    for i in range(0,22): # creating 22 empty corrals 
        corrals[f'corral_{i+1}'] = list()

    return pad, corrals

# PART 2: MODEL OPERATION
'''
FUNCTION 2.a: cart_addition 
This function will randomly add a cart to a corral every 2 seconds 
'''

def cart_addition(corrals): 
    while True: 
        random_corral = random.choice(list(corrals.keys()))
        corrals[random_corral].append('x')
        #print(f'cart added to {random_corral}')
        time.sleep(2)

'''
FUNCTION 2.b: cart_subtraction 
This function will randomly add a cart to a corral every 2 seconds 
'''
def cart_subtraction(qty_cart_pushers,pad, corrals): 
    while True: 
        for worker in range(qty_cart_pushers): # for now, this qty is just a number, not specific workers (this feature to be implemented later)
            '''
            I want to have a worker randomly select a corral to pick and take carts from, as soon as corral 
            So the logic should be: 
                1. randomly select a corral from corrals
                2. check if corral has at least 10 carts 
                3. remove 6 carts from corral 
            '''
            random_key = random.choice(list(corrals.keys())) #random.choice() returns a random element from a list, so need to cast corrals.keys() as a list
            
            corrals[random_key] = corrals[random_key][:-7] # the worker takes the last seven carts from corral
            
            #adding those 7 carts remove from the corral above to the pad: 
            for i in range(7): 
                pad.append('x')

            print(f'7 carts cleared from {random_key}.')
            time.sleep(5) # wait 5 seconds before the next worker retrieves 7 carts from randomly selected corral 
            
    

def main ():  
    #grabbing parameters for cart simulation
    cart_pushers, busy_rating = model_init()
    #print(f'There are {cart_pushers} cart pushers and the warehouse busy rating is {busy_rating}.')
    pad, corrals = lot_builder() 
    print(f'there are {len(corrals)} corrals in the lot')

    cart_addition(corrals)
    cart_subtraction(qty_cart_pushers = cart_pushers,pad = pad, corrals = corrals)

if __name__ == '__main__':

    main() 

