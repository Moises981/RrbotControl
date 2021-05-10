# DYNAMICS

## Langrange Formulation

**Equation for Joints:**

<img src="https://latex.codecogs.com/svg.image?\tau_i=\frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \dot q_i}-\frac{\partial \mathcal{L}}{\partial q_i}"/>

Where:

<img src="https://latex.codecogs.com/svg.image?\mathcal{L}"/> : Langrangian of the robot defined as the difference between the Kinetic Energy <img src="https://latex.codecogs.com/svg.image?\mathcal{L} = \tau"/> and Potential Energy <img src="https://latex.codecogs.com/svg.image?V"/> :

<img src="https://latex.codecogs.com/svg.image?\mathcal{L} = \tau-V"/>

## RRBOT

Spawn Rrbot in Gazebo:
```
roslaunch rrbot_gazebo spawn.launch
```

## Potential Energy and Kinetic Energy

**Potential Energy Equation:**

<img src="https://latex.codecogs.com/svg.image?E_p = mgh"/>

**Kinetic Energy Equation were described [here](Box.md).**

Where:
+ <img src="https://latex.codecogs.com/svg.image?m"/> : Mass
+ <img src="https://latex.codecogs.com/svg.image?g"/> : Gravity
+ <img src="https://latex.codecogs.com/svg.image?h"/> : Height

![Center of Mass Location](Images/CenterPosition.jpg))
