import random

def heuristic_action(state):
    """
    Implements an updated heuristic policy for Lunar Lander.
    Args:
        state (list): The state vector of the environment.
    Returns:
        int: The action to be taken.
    """
    x, y, vx, vy, angle, vang, leg1, leg2 = state
    
    # Define a threshold for being close to the ground
    close_to_floor = 0.1  # Threshold for y position (you may adjust based on the environment)
    
    # If the lander is close to the floor and is tilted, use the main engine to go up (action 2)
    if y < close_to_floor and (angle > 0.2 or angle < -0.2):
        return 2  # Main engine on to go up
    
    # If the lander is tilted to the right (angle too large), decide randomly between right engine or main engine
    elif angle > 0.2:
        return random.choice([3, 2])  # 50% chance between right engine (3) and main engine (2)
    
    # If the lander is tilted to the left (angle too small), decide randomly between left engine or main engine
    elif angle < -0.2:
        return random.choice([1, 2])  # 50% chance between left engine (1) and main engine (2)
    
    # If the angle is between -0.2 and 0.2, there is a 70% chance to activate the main engine
    elif -0.2 <= angle <= 0.2:
        if random.random() < 0.4:  # 70% chance
            return 2  # Activate main engine (action 2)
    
    # If the lander is rotating too fast in either direction, apply the respective rotation action
    elif vang > 0.2 or angle > 0.2:
        return 1  # Rotate left (correcting clockwise rotation)
    
    elif vang < -0.2 or angle < -0.2:
        return 3  # Rotate right (correcting counterclockwise rotation)
    
    # If one of the legs is on the ground, stop the engines
    elif leg1 or leg2:  # If either leg is on the ground
        return 0  # Stop engines
    
    # Default action: Do nothing (just hover)
    return 0  # Default action: Do nothing
