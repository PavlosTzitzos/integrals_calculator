Triple Integrals:
-----------------

Definition: $\int \int \int _A f(x,y,z) dx dy dz$

Cartesian Coordinates:
----------------------

<ins>Initially:</ins>

&emsp; &emsp; Focus only to make the triple integral into simple integrals of one variable.

&emsp; &emsp; Suppose that $x_1 , x_2 , y_1 , y_2 , z_1 , z_2\in R$ ,

&emsp; &emsp; $x_1(y,z)$ and $x_2(y,z)$ are functions of $y$ and $z$ ( $x=f(y,z)$ ) , 

&emsp; &emsp; $y_1(x,z)$ and $y_2(x,z)$ are functions of $x$ and $z$( $y=f(x,z)$ ) and

&emsp; &emsp; $z_1(x,y)$ and $z_2(x,y)$ are functions of $x$ and $y$ ( $z=f(x,y)$ ) .

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

&emsp; &emsp; Replace $x$ with $r \cdot \cos(\theta)$ and $y$ with $r \cdot \sin(\theta)$ :

&emsp; &emsp; $x(r,\theta) = r \cdot \cos(\theta)$ and $y(r,\theta) = r \cdot \sin(\theta)$ .

<ins>Step 2:</ins>

&emsp; &emsp; The new function is :

&emsp; &emsp; $f(r,\theta) = f( x(r,\theta) , y(r,\theta) ) \cdot r$

<ins>Step 3:</ins>

&emsp; &emsp; Compute integral with respect to $r$ and then to $\theta$ .

&emsp; &emsp; $\int_{ \theta _1} ^ {\theta _2} ( \int _{r_1} ^{r_2} f(r,\theta) dr ) d\theta $

**B.** For center of transformation $K(x_K,y_K)$ :

<ins>Step 1:</ins>

&emsp; &emsp; Replace $x$ with $r \cdot \cos(\theta) + x_K$ and $y$ with $r \cdot \sin(\theta) + y_K$ :

&emsp; &emsp; $x(r,\theta) = r \cdot \cos(\theta) + x_K$ and $y(r,\theta) = r \cdot \sin(\theta) + y_K$ .

<ins>Step 2:</ins>

&emsp; &emsp; The new function is :

&emsp; &emsp; $f(r,\theta) = f( x(r,\theta) , y(r,\theta) ) \cdot r$

<ins>Step 3:</ins>

&emsp; &emsp; Compute integral with respect to $r$ and then to $\theta$ .

&emsp; &emsp; $\int_{ \theta _1} ^ {\theta _2} ( \int _{r_1} ^{r_2} f(r,\theta) dr ) d\theta $


Cylindical Coordinates:
-----------------------

**A.** For center of transformation $O(0,0)$ :

<ins>Step 1:</ins>

&emsp; &emsp; Replace $x$ with $a \cdot r \cdot \cos(\theta)$ and $y$ with $b \cdot r \cdot \sin(\theta)$ :

&emsp; &emsp; $x(r,\theta) = a \cdot r \cdot \cos(\theta)$ and $y(r,\theta) = b \cdot r \cdot \sin(\theta)$ .

<ins>Step 2:</ins>

&emsp; &emsp; The new function is :

&emsp; &emsp; $f(r,\theta) = f( x(r,\theta) , y(r,\theta) ) \cdot r \cdot a \cdot b$

<ins>Step 3:</ins>

&emsp; &emsp; Compute integral with respect to $r$ and then to $\theta$ .

&emsp; &emsp; $\int_{ \theta _1} ^ {\theta _2} ( \int _{r_1} ^{r_2} f(r,\theta) dr ) d\theta $

**B.** For center of transformation $K(x_K,y_K)$ :

<ins>Step 1:</ins>

&emsp; &emsp; Replace $x$ with $a \cdot r \cdot \cos(\theta) + x_K$ and $y$ with $b \cdot r \cdot \sin(\theta) + y_K$ :

&emsp; &emsp; $x(r,\theta) = a \cdot r \cdot \cos(\theta) + x_K$ and $y(r,\theta) = b \cdot r \cdot \sin(\theta) + y_K$ .

<ins>Step 2:</ins>

&emsp; &emsp; The new function is :

&emsp; &emsp; $f(r,\theta) = f( x(r,\theta) , y(r,\theta) ) \cdot r \cdot a \cdot b$

<ins>Step 3:</ins>

&emsp; &emsp; Compute integral with respect to $r$ and then to $\theta$ .

&emsp; &emsp; $\int_{ \theta _1} ^ {\theta _2} ( \int _{r_1} ^{r_2} f(r,\theta) dr ) d\theta $


Ellipsoide Coordinates:
-----------------------



Paraboiled Coordinates:
----------------------


Conic Coordinates:
------------------

