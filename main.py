from agent import run_experiments
from visualize import plot_rewards

if __name__ == "__main__":
    num_episodes = 20  # Change if needed
    rewards_random, rewards_heuristic = run_experiments(num_episodes)
    plot_rewards(rewards_random, rewards_heuristic)
