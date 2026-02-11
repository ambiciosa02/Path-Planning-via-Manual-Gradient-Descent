# Path-Planning-via-Manual-Gradient-Descent

Project Overview
This script solves a navigation puzzle. Imagine a string stretched between a Start point and a Goal. Now, imagine a "Danger Zone" that pushes that string away.

The script uses a technique called Gradient Descent to find the perfect shape for that string—making it as short as possible while staying out of the "Danger Zone."

How the Path "Learns"
Instead of guessing, the path adjusts itself slightly over 2,000 small steps:

Goal Seeking: The end of the path is constantly pulled toward the Gold Star.

Path Smoothing: Each point on the line tries to stay close to its neighbors to avoid jagged edges.

Obstacle Avoidance: If any part of the path dips into the "High Cost Zone" (the red area), it feels a "push" that forces it upward into the safe white space.

<img width="1000" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/2cfe29fd-4a9c-4a7a-890f-29409498c3bb" />

🛠️ Key Features
From-Scratch Logic: No complex AI libraries—just pure logic and movement rules.

Visual Simulation: Watch the final path curve perfectly around the restricted area.

Customizable: Easily change the start point, the goal, or the "danger" threshold in the code.


