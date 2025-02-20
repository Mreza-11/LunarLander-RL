import gymnasium as gym

def create_env(render_mode="human"):
    """
    Creates and returns the LunarLander environment.
    Args:
        render_mode (str): Set to 'human' for visualization, otherwise None.
    Returns:
        env (gym.Env): The initialized Gymnasium environment.
    """
    return gym.make('LunarLander-v3', render_mode=render_mode)
