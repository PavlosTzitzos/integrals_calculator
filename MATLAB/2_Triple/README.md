Triple Integrals:
-----------------

Definition: $\int \int \int _A f(x,y,z) dx dy dz$

Cartesian Coordinates:
----------------------

<ins>Initially:</ins>

&emsp; &emsp; Focus only to make the triple integral into simple integrals of one variable.

&emsp; &emsp; Suppose that $x_1 , x_2 , y_1 , y_2 , z_1 , z_2\in R$ ,

&emsp; &emsp; $x_1(y,z)$ and $x_2(y,z)$ are functions of $y$ and / or $z$ ( $x=f(y,z)$ ) , 

&emsp; &emsp; $y_1(x,z)$ and $y_2(x,z)$ are functions of $x$ and / or $z$( $y=f(x,z)$ ) and

&emsp; &emsp; $z_1(x,y)$ and $z_2(x,y)$ are functions of $x$ and / or $y$ ( $z=f(x,y)$ ) .

<ins>Step 1:</ins>

&emsp; &emsp; If $A$ is known then choose the apropriate case:

&emsp; &emsp; case 1: &emsp; &emsp; $A=$ { $(x,y,z): x_1 \leq x \leq x_2 ~ and ~ y_1 \leq y \leq y_2 ~ and ~ z_1 \leq z \leq z_2$ }

&emsp; &emsp; case 2: &emsp; &emsp; $A=$ { $(x,y,z): (x,y) \in D ~ and ~ z_1(x,y) \leq z \leq z_2(x,y)$ }

&emsp; &emsp; case 3: &emsp; &emsp; $A=$ { $(x,y,z): (x,z) \in D ~ and ~ y_1(x,z) \leq y \leq y_2(x,z)$ }

&emsp; &emsp; case 4: &emsp; &emsp; $A=$ { $(x,y,z): (y,z) \in D ~ and ~ x_1(y,z) \leq x \leq x_2(y,z)$ }

** Note : these are the only cases that have an analytical solution.

<ins>Step 2:</ins>

&emsp; &emsp; Integrate according to the case.

&emsp; &emsp; case 1: &emsp; &emsp; $\int_{x_1} ^{x_2} ( \int_{y_1} ^{y_2} ( \int_{z_1} ^{z_2} f(x,y,z) dz ) dy ) dz$

&emsp; &emsp; case 2: &emsp; &emsp; $I_1 = \int_{z_1(x,y)} ^{z_2(x,y)} f(x,y,z) dz$

&emsp; &emsp; case 3: &emsp; &emsp; $I_1 = \int_{y_1(x,z)} ^{y_2(x,z)} f(x,y,z) dy$

&emsp; &emsp; case 4: &emsp; &emsp; $I_1 = \int_{x_1(y,z)} ^{x_2(y,z)} f(x,y,z) dx$

<ins>Step 3:</ins>

&emsp; &emsp; Use double integral for the other 2 variables.



Spherical Coordinates:
----------------------

**A.** For center of transformation $O(0,0)$ :

<ins>Step 1:</ins>

&emsp; &emsp; Replace :

&emsp; &emsp; $x(r,\theta , \phi) = r \cdot \sin(\theta) \cdot \cos(\phi)$ , 

&emsp; &emsp; $y(r,\theta , \phi) = r \cdot \sin(\theta) \cdot \sin(\phi)$ , 

&emsp; &emsp; $z(r,\theta , \phi) = r \cdot \cos(\theta)$ .

<ins>Step 2:</ins>

&emsp; &emsp; The new function is :

&emsp; &emsp; $f(r,\theta , \phi) = f( x(r,\theta , \phi) , y(r,\theta , \phi) , z(r,\theta , \phi) ) \cdot r^2 \cdot sin( \theta)$

<ins>Step 3:</ins>

&emsp; &emsp; Compute integral with respect to $r$ , then to $\theta$ and then to $\phi$.

&emsp; &emsp; $\int_{ \phi_1} ^{ \phi_2} ( \int_{ \theta _1} ^ {\theta _2} ( \int _{r_1} ^{r_2} f(r,\theta,\phi) dr ) d\theta ) d\phi$

**B.** For center of transformation $K(x_K,y_K,z_K)$ :

<ins>Step 1:</ins>

&emsp; &emsp; Replace :

&emsp; &emsp; $x(r,\theta , \phi) = r \cdot \sin(\theta) \cdot \cos(phi) + x_K$ , 

&emsp; &emsp; $y(r,\theta , \phi) = r \cdot \sin(\theta) \cdot \sin(phi) + y_K$ , 

&emsp; &emsp; $z(r,\theta , \phi) = r \cdot \cos(\theta) + z_K$ .

<ins>Step 2:</ins>

&emsp; &emsp; The new function is :

&emsp; &emsp; $f(r,\theta , \phi) = f( x(r,\theta , \phi) , y(r,\theta , \phi) , z(r,\theta , \phi) ) \cdot r^2 \cdot sin( \theta)$

<ins>Step 3:</ins>

&emsp; &emsp; Compute integral with respect to $r$ , then to $\theta$ and then to $\phi$.

&emsp; &emsp; $\int_{ \phi_1} ^{ \phi_2} ( \int_{ \theta _1} ^ {\theta _2} ( \int _{r_1} ^{r_2} f(r,\theta,\phi) dr ) d\theta ) d\phi$


Cylindical Coordinates:
-----------------------

**A.** For center of transformation $O(0,0)$ :

<ins>Step 1:</ins>

&emsp; &emsp; Replace :

&emsp; &emsp; $x(\rho , \phi , z) = rho \cdot \cos(\phi)$ , 

&emsp; &emsp; $y(\rho , \phi , z) = rho \cdot \sin(\phi)$ , 

&emsp; &emsp; $z(\rho , \phi , z) = z$ .

<ins>Step 2:</ins>

&emsp; &emsp; The new function is :

&emsp; &emsp; $f(\rho,\phi,z) = f( x(\rho , \phi , z) , y(\rho , \phi , z) , z(\rho , \phi , z) ) \cdot \rho $

<ins>Step 3:</ins>

&emsp; &emsp; Compute integral with respect to $\rho$ , then $\phi$ and then $z$ :

&emsp; &emsp; $\int_{ z_1} ^ { z_2} ( \int _{ \phi _1} ^{ \phi _2} ( \int_{ \rho _1} ^{ \rho _2} f( \rho , \phi , \z ) d\rho ) d\phi ) dz$ .

**B.** For center of transformation $K(x_K,y_K)$ :

<ins>Step 1:</ins>

&emsp; &emsp; Replace :

&emsp; &emsp; $x(\rho , \phi , z) = rho \cdot \cos(\phi) + x_K$ , 

&emsp; &emsp; $y(\rho , \phi , z) = rho \cdot \sin(\phi) + y_K$ , 

&emsp; &emsp; $z(\rho , \phi , z) = z + z_K$ .

<ins>Step 2:</ins>

&emsp; &emsp; The new function is :

&emsp; &emsp; $f(\rho,\phi,z) = f( x(\rho , \phi , z) , y(\rho , \phi , z) , z(\rho , \phi , z) ) \cdot \rho$

<ins>Step 3:</ins>

&emsp; &emsp; Compute integral with respect to $\rho$ , then $\phi$ and then $z$ :

&emsp; &emsp; $\int_{ z_1} ^ { z_2} ( \int _{ \phi _1} ^{ \phi _2} ( \int_{ \rho _1} ^{ \rho _2} f( \rho , \phi , \z ) d\rho ) d\phi ) dz$ .


Ellipsoide Coordinates:
-----------------------

** Note: the only simple difference with spherical coordinates are the a , b and c parameters of the ellipsoid.

**A.** For center of transformation $O(0,0)$ :

<ins>Step 1:</ins>

&emsp; &emsp; Replace :

&emsp; &emsp; $x(r,\theta , \phi) = a \cdot r \cdot \sin(\theta) \cdot \cos(\phi)$ , 

&emsp; &emsp; $y(r,\theta , \phi) = b \cdot r \cdot  \sin(\theta) \cdot \sin(\phi)$ , 

&emsp; &emsp; $z(r,\theta , \phi) = c \cdot r \cdot  \cos(\theta)$ .

<ins>Step 2:</ins>

&emsp; &emsp; The new function is :

&emsp; &emsp; $f(r,\theta , \phi) = f( x(r,\theta , \phi) , y(r,\theta , \phi) , z(r,\theta , \phi) ) \cdot a \cdot b \cdot c \cdot r^2 \cdot sin( \theta)$

<ins>Step 3:</ins>

&emsp; &emsp; Compute integral with respect to $r$ , then to $\theta$ and then to $\phi$.

&emsp; &emsp; $\int_{ \phi_1} ^{ \phi_2} ( \int_{ \theta _1} ^ {\theta _2} ( \int _{r_1} ^{r_2} f(r,\theta,\phi) dr ) d\theta ) d\phi$

**B.** For center of transformation $K(x_K,y_K,z_K)$ :

<ins>Step 1:</ins>

&emsp; &emsp; Replace :

&emsp; &emsp; $x(r,\theta , \phi) = a \cdot r \cdot \sin(\theta) \cdot \cos(phi) + x_K$ , 

&emsp; &emsp; $y(r,\theta , \phi) = b \cdot r \cdot \sin(\theta) \cdot \sin(phi) + y_K$ , 

&emsp; &emsp; $z(r,\theta , \phi) = c \cdot r \cdot \cos(\theta) + z_K$ .

<ins>Step 2:</ins>

&emsp; &emsp; The new function is :

&emsp; &emsp; $f(r,\theta , \phi) = f( x(r,\theta , \phi) , y(r,\theta , \phi) , z(r,\theta , \phi) ) \cdot a \cdot b \cdot c \cdot r^2 \cdot sin( \theta)$

<ins>Step 3:</ins>

&emsp; &emsp; Compute integral with respect to $r$ , then to $\theta$ and then to $\phi$.

&emsp; &emsp; $\int_{ \phi_1} ^{ \phi_2} ( \int_{ \theta _1} ^ {\theta _2} ( \int _{r_1} ^{r_2} f(r,\theta,\phi) dr ) d\theta ) d\phi$



Paraboiled Coordinates:
----------------------


Conic Coordinates:
------------------

