import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt

# Initialize the Lunar Lander environment
env = gym.make('LunarLander-v3', render_mode='human')

# Define a better heuristic function
def heuristic_action(state):
    x, y, vx, vy, angle, vang, leg1, leg2 = state
    if y > 0.5 and vy < -0.1:
        return 2  # Fire main engine
    elif angle > 0.2 or vang > 0.2:
        return 1  # Rotate left
    elif angle < -0.2 or vang < -0.2:
        return 3  # Rotate right
    elif leg1 or leg2:  # If one of the legs is on the ground, stop engines
        return 0
    return 0  # Do nothing

# Lists to store rewards
rewards_random = []
rewards_heuristic = []

# Run 20 episodes with random actions
for episode in range(20):
    state, _ = env.reset()
    total_reward = 0
    done = False
    while not done:
        action = env.action_space.sample()
        next_state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
        total_reward += reward
        state = next_state
    rewards_random.append(total_reward)

# Run 20 episodes with heuristic actions
for episode in range(20):
    state, _ = env.reset()
    total_reward = 0
    done = False
    while not done:
        action = heuristic_action(state)
        next_state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
        total_reward += reward
        state = next_state
    rewards_heuristic.append(total_reward)

# Compute mean and standard deviation of rewards
mean_random = np.mean(rewards_random)
std_random = np.std(rewards_random)
mean_heuristic = np.mean(rewards_heuristic)
std_heuristic = np.std(rewards_heuristic)

print(f"Random Actions - Mean Reward: {mean_random:.2f}, Std: {std_random:.2f}")
print(f"Heuristic Actions - Mean Reward: {mean_heuristic:.2f}, Std: {std_heuristic:.2f}")

# Close the environment
env.close()

# ==========================
# Visualization of Performance
# ==========================

# 1. Plot Reward Progression over Episodes
plt.figure(figsize=(12, 5))
plt.plot(rewards_random, label="Random Actions", marker='o', linestyle='dashed', color='red')
plt.plot(rewards_heuristic, label="Heuristic Actions", marker='s', linestyle='solid', color='blue')
plt.xlabel("Episode")
plt.ylabel("Total Reward")
plt.title("Total Rewards over 20 Episodes")
plt.legend()
plt.grid(True)
plt.show()

# 2. Histogram Comparison of Reward Distribution
plt.figure(figsize=(10, 5))
plt.hist(rewards_random, bins=10, alpha=0.7, color='red', label="Random Actions")
plt.hist(rewards_heuristic, bins=10, alpha=0.7, color='blue', label="Heuristic Actions")
plt.xlabel("Total Reward")
plt.ylabel("Frequency")
plt.title("Distribution of Rewards")
plt.legend()
plt.grid(True)
plt.show()
