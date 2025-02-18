# Lab 3: Projectile Motion under Air Resistance

This repository contains the code and documentation for **Lab 3**, which investigates the effects of **air resistance** on the motion of projectiles. The lab focuses on solving **Newton's 2nd law** numerically to analyze how air resistance impacts the trajectory, velocity, and position of falling objects and projectiles. By comparing results with and without air resistance, you will gain insights into when air resistance can be neglected and when it plays a significant role.

## Key Concepts
- **Air resistance modeling**: The resistive force is modeled as \( F = bV + cV^2 \), where \( b \) and \( c \) depend on the object's size and shape.
- **Terminal velocity**: The maximum velocity reached when air resistance balances gravitational force.
- **Numerical integration**: Using small time steps (\( \Delta t \)) to solve differential equations for velocity and position.
- **Trajectory analysis**: Comparing parabolic trajectories (no air resistance) with realistic trajectories (with air resistance).

## Lab Structure

The lab is divided into four exercises:

### 1. **Air Resistance Scaling with Velocity**
- Plot the contributions of the linear (\( bV \)) and quadratic (\( cV^2 \)) terms to the air resistance force.
- Determine the ranges of velocity and object size where each term dominates.
- Analyze specific cases (e.g., baseball, oil drop, raindrop) to identify the ideal form of \( f(V) \).

### 2. **Vertical Motion under Air Resistance**
- Simulate the vertical motion of a spherical grain of dust released from rest.
- Compare numerical results with the analytical solution for velocity as a function of time.
- Investigate how mass affects the time to reach the ground and discuss the validity of the "all objects fall at the same rate" statement.

### 3. **Projectile Motion with Linear Air Resistance**
- Simulate the trajectory of a projectile launched at an angle \( \theta \) with linear air resistance (\( c = 0 \)).
- Compare the trajectory with and without air resistance.
- Determine the optimal launch angle for maximum horizontal displacement and analyze its dependence on mass.

### 4. **Projectile Motion with Quadratic Air Resistance**
- Extend the simulation to include quadratic air resistance (\( b = 0 \)).
- Solve coupled differential equations for horizontal and vertical motion.
- Compare trajectories for linear, quadratic, and no air resistance cases under varying conditions (mass, launch angle, initial velocity).

## Repository Contents
- **Python scripts** for each exercise, including numerical integration and trajectory plotting.
- **Plots** and visualizations of velocity, position, and trajectories.

This lab provides a hands-on introduction to **computational physics** and the importance of air resistance in projectile motion. Feel free to explore and adapt the code for your own projects!
