def heuristic_action(state):
    """
    Implements a simple heuristic policy for Lunar Lander.
    Args:
        state (list): The state vector of the environment.
    Returns:
        int: The action to be taken.
    """
    x, y, vx, vy, angle, vang, leg1, leg2 = state
    if angle > 0.2 or vang > 0.2:
        return 1  # Rotate left
    elif angle < -0.2 or vang < -0.2:
        return 3  # Rotate right
    elif leg1 or leg2:  # If one of the legs is on the ground, stop engines
        return 0
    return 0  # Default action: Do nothing
