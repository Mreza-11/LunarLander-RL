import gymnasium as gym
import numpy as np

# انتخاب محیط Lunar Lander
env = gym.make('LunarLander-v3', render_mode='human')

# تعریف یک heuristic ساده
def heuristic_action(state):
    x, y, vx, vy, angle, vang, leg1, leg2 = state  # Unpack the state vector
    if y > 0.5 and vy < -0.1:
        return 2  # روشن کردن موتور پایینی
    elif angle > 0.1:
        return 1  # چرخش به چپ
    elif angle < -0.1:
        return 3  # چرخش به راست
    else:
        return 0  # هیچ کاری نکن

# لیست برای ذخیره پاداش‌ها
rewards_random = []
rewards_heuristic = []

# اجرای 20 اپیزود با اعمال تصادفی
for episode in range(20):
    state, _ = env.reset()  # Unpack the state and ignore the info dictionary
    total_reward = 0
    done = False
    while not done:
        action = env.action_space.sample()  # انتخاب عمل تصادفی
        next_state, reward, done, _, _ = env.step(action)  # Unpack the next state and ignore other values
        total_reward += reward
        state = next_state
    rewards_random.append(total_reward)

# اجرای 20 اپیزود با اعمال heuristic
for episode in range(20):
    state, _ = env.reset()  # Unpack the state and ignore the info dictionary
    total_reward = 0
    done = False
    while not done:
        action = heuristic_action(state)  # انتخاب عمل بر اساس heuristic
        next_state, reward, done, _, _ = env.step(action)  # Unpack the next state and ignore other values
        total_reward += reward
        state = next_state
    rewards_heuristic.append(total_reward)

# محاسبه میانگین و انحراف معیار پاداش‌ها
mean_random = np.mean(rewards_random)
std_random = np.std(rewards_random)
mean_heuristic = np.mean(rewards_heuristic)
std_heuristic = np.std(rewards_heuristic)

print(f"Random Actions - Mean Reward: {mean_random}, Std: {std_random}")
print(f"Heuristic Actions - Mean Reward: {mean_heuristic}, Std: {std_heuristic}")

# بستن محیط
env.close()