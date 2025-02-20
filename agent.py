import numpy as np
from environment import create_env
from heuristic import heuristic_action

def run_episode(env, policy="random"):
    """
    Runs a single episode of Lunar Lander.
    Args:
        env (gym.Env): The environment instance.
        policy (str): "random" for random actions, "heuristic" for heuristic policy.
    Returns:
        float: Total reward accumulated in the episode.
    """
    state, _ = env.reset()
    total_reward = 0
    done = False
    
    while not done:
        if policy == "random":
            action = env.action_space.sample()  # Random action
        elif policy == "heuristic":
            action = heuristic_action(state)  # Heuristic action
        else:
            raise ValueError("Invalid policy. Choose 'random' or 'heuristic'.")

        next_state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
        total_reward += reward
        state = next_state
    
    return total_reward

def run_experiments(num_episodes=20):
    """
    Runs multiple episodes for both random and heuristic agents.
    Args:
        num_episodes (int): Number of episodes to run for each agent.
    Returns:
        tuple: Rewards for random and heuristic agents.
    """
    env = create_env()
    
    rewards_random = [run_episode(env, policy="random") for _ in range(num_episodes)]
    rewards_heuristic = [run_episode(env, policy="heuristic") for _ in range(num_episodes)]
    
    env.close()
    
    return rewards_random, rewards_heuristic
