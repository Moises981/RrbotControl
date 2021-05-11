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

### Center of Mass Position XY of Joints - Explanation

![Center of Mass Location](Images/CenterPosition.jpg))
Run command to monitore data:
```
rosrun rrbot_monitor dynamics_monitor.py
```
Run command to bag data:
```
rosservice call /gazebo/reset_simulation && \
rosbag record /dynamic_data --duration=30 \
  --output-name=data.bag
```
Run command to show plot:
```
rosrun rrbot_monitor bag_monitor.py
```
![Physics](Images/Plots.png))





