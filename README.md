# RRBOT DYNAMICS

## Center of Mass
<link rel="stylesheet" type="text/css" media="all" href="documentation/md_styles.css" />

Equation:

<img src="https://latex.codecogs.com/svg.image?R=\frac{1}{M}\int_{V}\rho(r)rdV"/>

Where:
+ M : Total mass of object
+ <img src="https://latex.codecogs.com/svg.image?\rho"/> : Density
+ V : Volume
+ R : Center of Mass 

## Kinetic Energies

**Translational Equation:**

<img src="https://latex.codecogs.com/svg.image?E_t=\frac{1}{2}Mv_c^2"/>

Where:
+ <img src="https://latex.codecogs.com/svg.image?E_t"/> : Kinetic Energy 
+ <img src="https://latex.codecogs.com/svg.image?\rho"/> : Density
+ V : Speed of center of mass

**Rotational Equation:**

<img src="https://latex.codecogs.com/svg.image?E_r=\int_{M}\frac{v^2dm}{2}=\frac{1}{2}I\omega^2"/>

Where:
+ <img src="https://latex.codecogs.com/svg.image?\omega"/> : Angular Velocity
+ <img src="https://latex.codecogs.com/svg.image?I"/> : Moment of Inertia
+ M : Total mass of object

**Total Kinetic Energy Equation:**

<img src="https://latex.codecogs.com/svg.image?E_k=E_t+E_r">


## Moments of Inertia

**Force Equation:**

<img src="https://latex.codecogs.com/svg.image?f=ma">

Where:
+ <img src="https://latex.codecogs.com/svg.image?f"/> : Force
+ <img src="https://latex.codecogs.com/svg.image?m"/> : Mass
+ <img src="https://latex.codecogs.com/svg.image?a"/> : Acceleration

**Torque Equation:**

<img src="https://latex.codecogs.com/svg.image?\tau=Ia">

Where:
+ <img src="https://latex.codecogs.com/svg.image?\tau"/> : Torque
+ <img src="https://latex.codecogs.com/svg.image?I"/> : Inertia
+ <img src="https://latex.codecogs.com/svg.image?a"/> : Acceleration

**Inertia Equation:**

<img src="https://latex.codecogs.com/svg.image?I=\int_{V}r^2\rho(r)dV"/>

Where:
+ <img src="https://latex.codecogs.com/svg.image?r"/> : Continuous mass distribution
+ <img src="https://latex.codecogs.com/svg.image?\rho"/> : Density
+ <img src="https://latex.codecogs.com/svg.image?v"/> : Volume



## Box Dimmensions:
+ Height: 30cm
+ Width : 40cm
+ Depth : 50cm

## Calculate Inertia from Torque

Apply torque to rotate box:
```
rosrun box_properties apply_torque.py
```

**Equation:**

<img src="https://latex.codecogs.com/svg.image?I=\frac{T\tau}{\omega-\omega_0}"/>

Since <img src="https://latex.codecogs.com/svg.image?\omega_0=0"/> and <img src="https://latex.codecogs.com/svg.image?T=0"/>

<img src="https://latex.codecogs.com/svg.image?I=\frac{\tau}{\omega}"/>


## Commands:

Compute Inertia from Box:
```
rosrun box_properties compute_moments.py
```
Reset world:
```
rosservice call /gazebo/reset_world "{}"
```

