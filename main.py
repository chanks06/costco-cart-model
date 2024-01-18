# COSTCO PARKING LOT CART MANAGEMENT MODEL 

#libraries:
import time 
import random 
import threading
import keyboard 

# PART 1: MODEL SET UP 

stop_event = threading.Event()

def push_to_stop(): 
    global stop_event 
    keyboard.wait('space')
    
    while True:
        if keyboard.is_pressed('space'):
            stop_event.set()
            print(stop_event)
            break
        time.sleep(0.1) 

'''
FUNCTION 1.a: PARAMETERS 
Parameter retrieval function: ask the user the following questions:
1. How many cart pushers are working ? 
2. How busy is the warehouse (on a scale of 0 to 10) ? 
'''

def model_init(): 
    qty_cart_pushers = int(input('How many cart pushers are working (0 - 6) ?    '))
    busy_rating = int(input('How busy is the warehouse (0 - 10) ?    '))

    return qty_cart_pushers, busy_rating


'''
FUNCTION 1.b: DISPLAY LOT 
when called this function displays current state of parking lot corrals 
'''

def display_lot(corrals):
    for corral_key, corral_value in corrals.items(): 
        print(f'{corral_key}: {corral_value}')


'''
FUNCTION 1.c: CREATE CORRALS
There are 22 corrals on site, each with a capacity of 24 carts (before considered overflowing)
There is 1 pad, which has a initial number of carts of 24 * 4 = 96
'''
def lot_builder(): 
    pad = [] # var pad is a list 
    corrals = {} # var corrals is a dictionary of lists 
    
    for i in range(0,22): # creating 22 empty corrals 
        corrals[f'corral_{i+1}'] = list('x'*10)

    return pad, corrals

'''
FUNCTION 1.d: STOP THREADS
This function is to stop the program and to display the resulting parking lot 
'''




# PART 2: MODEL OPERATION
    
'''
FUNCTION 2.a: cart_addition 
This function will randomly add a cart to a corral every 2 seconds 
'''
def cart_addition(corrals): 
    global stop_event
    while not stop_event.is_set(): 
        random_corral = random.choice(list(corrals.keys()))
        corrals[random_corral].append('x')
        print(f'cart added to {random_corral}')
        time.sleep(1)



'''
FUNCTION 2.b: cart_subtraction 
This function will randomly add a cart to a corral every 5 seconds 
'''

def cart_subtraction(qty_cart_pushers,pad, corrals): 
    global stop_event
    while not stop_event.is_set(): 
        for worker in range(qty_cart_pushers): # for now, this qty is just a number, not specific workers (this feature to be implemented later)
            '''
            I want to have a worker randomly select a corral to pick and take carts from, as soon as corral 
            So the logic should be: 
                1. randomly select a corral from corrals
                2. check if corral has at least 10 carts 
                3. remove 6 carts from corral 
            '''
            random_key = random.choice(list(corrals.keys())) #random.choice() returns a random element from a list, so need to cast corrals.keys() as a list
            
            if len(corrals[random_key]) >= 7:
            
                corrals[random_key] = corrals[random_key][:-7] # the worker takes the last seven carts from corral
                                                              #adding those 7 carts remove from the corral above to the pad: 
                print(f'7 carts cleared from {random_key}.')
            else: 
                pass

            time.sleep(5) # wait 5 seconds before the next worker retrieves 7 carts from randomly selected corral 
            
    



#main 
def main (): 

    #Intro statement 
    print("========================================================================================================")
    print("WELCOME TO COSTCO WAREHOUSE #97 in Clackamas, OR.")
    print("This program simulates the movement of shopping carts between the corrals and the pad in the parking lot.")
    print("========================================================================================================")

    # Pause for 3 seconds
    time.sleep(3)

    # Print information about carts and corrals with separators
    print("\nEach cart is represented by an 'x'.")
    print("\nEach corral is one of twenty-two lists inside the Corral Dictionary.")
    time.sleep(5)
    print("\nWhile the program is running, you may press spacebar to stop the simulation and view the final result of the corrals and pad.")
    print("\nLet us begin!\n")



    #grabbing parameters for cart simulation
    cart_pushers, busy_rating = model_init()
    pad, corrals = lot_builder() 

    #creating addition and substraction threads 
    thread_addition = threading.Thread(target=cart_addition, args = (corrals,))
    thread_subtraction = threading.Thread(target=cart_subtraction, args = (cart_pushers, pad, corrals))

    display_lot(corrals) # show initial state of lot
    time.sleep(5) # take a breath 

    #starting keyboard event thread 
    stop_thread = threading.Thread(target = push_to_stop, args = ())
    stop_thread.start()


    thread_addition.start()
    thread_subtraction.start()

    stop_thread.join()

    stop_event.set() #this stops the program 

    thread_addition.join()
    thread_subtraction.join()
    

    print("Final state of Parking Lot: ")
    display_lot(corrals)



if __name__ == '__main__':

    main() 

