import matplotlib.pyplot as plt
import numpy as np

def plot_rewards(rewards_random, rewards_heuristic):
    """
    Plots reward progression over episodes and distribution.
    Args:
        rewards_random (list): List of total rewards for random actions.
        rewards_heuristic (list): List of total rewards for heuristic actions.
    """
    # Compute statistics
    mean_random = np.mean(rewards_random)
    std_random = np.std(rewards_random)
    mean_heuristic = np.mean(rewards_heuristic)
    std_heuristic = np.std(rewards_heuristic)

    print(f"Random Actions - Mean Reward: {mean_random:.2f}, Std: {std_random:.2f}")
    print(f"Heuristic Actions - Mean Reward: {mean_heuristic:.2f}, Std: {std_heuristic:.2f}")

    # Plot Reward Progression
    plt.figure(figsize=(12, 5))
    plt.plot(rewards_random, label="Random Actions", marker='o', linestyle='dashed', color='red')
    plt.plot(rewards_heuristic, label="Heuristic Actions", marker='s', linestyle='solid', color='blue')
    plt.xlabel("Episode")
    plt.ylabel("Total Reward")
    plt.title("Total Rewards over Episodes")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Histogram of Reward Distribution
    plt.figure(figsize=(10, 5))
    plt.hist(rewards_random, bins=10, alpha=0.7, color='red', label="Random Actions")
    plt.hist(rewards_heuristic, bins=10, alpha=0.7, color='blue', label="Heuristic Actions")
    plt.xlabel("Total Reward")
    plt.ylabel("Frequency")
    plt.title("Distribution of Rewards")
    plt.legend()
    plt.grid(True)
    plt.show()
