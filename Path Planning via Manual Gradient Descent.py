import numpy as np
import matplotlib.pyplot as plt

# 1. Configuration
n_iterations = 2000
learning_rate = 0.01
constraint_y = 2
start_pos = np.array([0.0, 0.0])
goal_pos = np.array([10.0, 5.0])

# Initialize path: A straight line from start to goal
n_points = 10
path = np.linspace(start_pos, goal_pos, n_points)

def get_gradients(path):
    grad = np.zeros_like(path)
    
    # We don't move the Start point (index 0)
    for i in range(1, n_points):
        point = path[i]
        
        # --- Gradient 1: Move toward Goal (Attractive force) ---
        # For the last point, pull it to the star. For others, pull toward neighbor.
        if i == n_points - 1:
            grad[i] += 2 * (point - goal_pos) 
        else:
            # Smoothing: pull toward the next point to keep path short
            grad[i] += 0.5 * (point - path[i+1])
            grad[i] += 0.5 * (point - path[i-1])

        # --- Gradient 2: Avoid Constraint (Repulsive force) ---
        # If y < 2, the gradient points UP (positive y) to push it out.
        if point[1] < constraint_y:
            # The deeper it is, the stronger the push
            grad[i][1] -= 15 * (constraint_y - point[1]) 
            
    return grad

# 2. Optimization Loop (The Descent)
history = []
for _ in range(n_iterations):
    g = get_gradients(path)
    path -= learning_rate * g  # Move opposite to gradient
    history.append(path.copy())

# 3. Visualization
plt.figure(figsize=(10, 6))

# Draw the "Expensive" zone
plt.axhspan(-1, constraint_y, color='red', alpha=0.1, label="High Cost Zone")
plt.axhline(y=constraint_y, color='red', linestyle='--', linewidth=2)

# Plot the final path
plt.plot(path[:, 0], path[:, 1], 'b-o', label='Optimized Path')
plt.scatter(*start_pos, color='green', s=100, label='Start')
plt.scatter(*goal_pos, color='gold', marker='*', s=300, label='Goal')

plt.title("Path Planning via Manual Gradient Descent")
plt.ylim(-1, 6)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()