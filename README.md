# COSTCO SHOPPING CART MODEL 


I would like to create a simulation of how the shopping carts populate and are wrangled by workers in the costco parking lot. This project is inspired by my current work as a front-end assistant at Costco warehouse #97. Part of the job is gathering shopping carts and pushing a train of them from their corrals across the parking lot and back to the front of the warehouse. 

1. Define the Entities:

    Shopping Carts: Each cart could be represented as an object with attributes like an ID, capacity, and current occupancy.
    Corrals: Represent areas where shopping carts are stored.
    Workers: Model the workers who fetch and organize the carts.

2. Simulation Parameters:

    Warehouse Busyness: A parameter that influences how quickly corrals get filled or emptied based on customer activity.
    Number of Workers: A parameter that affects the rate at which workers fetch carts.
    Corral Capacity: The maximum number of carts a corral can hold.

3. Simulation Logic:

    Corral Population: Simulate how carts are added to corrals over time. The rate might be influenced by the busyness parameter.
    Worker Activities: Simulate the workers fetching carts. The number of workers and their efficiency could be factors.
    Corral Overflow: If a corral exceeds its capacity, simulate the excess carts spilling out or being redistributed to other corrals.