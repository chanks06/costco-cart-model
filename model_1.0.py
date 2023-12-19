# objective - write a program that adds and subtracts carts from the corrals. 



#libraries 
import time 
import random 

#parameters 
workers = ['charles', 'chris'] # for now, workers is a list of strings, but will add worker objects with variable attributes

corrals = {} # the corrals is a dictionary of lists. Each cart is an 'x' within each list. 
for i in range(0,4):
    corrals[f'corral_{i+1}'] = list('x' * 10) # each corral begins with 10 carts.

#utility functions
def random_corral(corrals): 
    key = random.choice(list(corrals.keys()))
    return key 

def cart_addition(corrals): 
    while True: 
        chosen_corral = random_corral(corrals) # randomly choosing a corral 
        corrals[chosen_corral].append('x') # adding one cart to a randomly selected corral

        if len(corrals[chosen_corral]) > 24: 
            print(f'{chosen_corral} is overflowing')
    
        time.sleep(1) #function sleeps for 1 second, and then repeats}

def cart_subtraction(workers, corrals): 
    while True: 
        for worker in workers: 
            '''
            let's assume var workers is a list of worker names
            I want to have a worker randomly select a corral to pick and take carts from, as soon as corral as at least 10 carts!
            So the logic should be: 
                1. randomly select a corral from corrals
                2. check if corral has at least 10 carts 
                3. remove 6 carts from corral 
            '''
            corral_sub =  random.choice() 
                
            while len(corrals[corral_sub]) < 10: #continue randomly selecting a corral until you find one that has at 
                                                #least 10 carts (this emulates the behavoir of a cart pusher who would seek out a corral in the parking lot that is worth pulling form)
                corral_sub = random_corral(corrals)

            else:  
            #if that corral has at at least 10 carts 
            # remove the last 7 elements from the list 
                corrals[corral_sub] = corrals[corral_sub][:-7]
                print(f'{worker} retrieved 7 carts from {corral_sub}.')

                time.sleep(5) # wait 5 seconds before the next worker retrieves carts 
                
def main ():  
    cart_addition(corrals = corrals)
    cart_subtraction(workers = workers, corrals = corrals)
    
    
if __name__ == '__main__':
    main() 
