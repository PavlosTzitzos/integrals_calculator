Double Integrals:
-----------------
Definition: $\int \int _D f(x,y) dx dy$

Cartesian Coordinates:
----------------------

<ins>Initally:</ins>

&emsp; &emsp; Focus only to make the double integral into simple integrals of one variable.

<ins>Step 1:</ins>

&emsp; &emsp; If $D$ is known then choose the apropriate case:

&emsp; &emsp; case 1: &emsp; &emsp; $D=$ { $(x,y\): a \leq x \leq b ~ and ~ c \leq y \leq d$ }

&emsp; &emsp; case 2: &emsp; &emsp; $D=$ { $(x,y): a \leq x \leq x_2 (y) ~ and ~ c \leq y \leq d$ }

&emsp; &emsp; case 3: &emsp; &emsp; $D=$ { $(x,y): x_1 (y) \leq x \leq b ~ and ~ c \leq y \leq d$ }

&emsp; &emsp; case 4: &emsp; &emsp; $D=$ { $(x,y): x_1 (y) \leq x \leq x_2 (y) ~ and ~ c \leq y \leq d$ }

&emsp; &emsp; case 5: &emsp; &emsp; $D=$ { $(x,y): a \leq x \leq b ~ and ~ y_1 (x) \leq y \leq d$ }

&emsp; &emsp; case 6: &emsp; &emsp; $D=$ { $(x,y): a \leq x \leq b ~ and ~ c \leq y \leq y_2 (x)$ }

&emsp; &emsp; case 7: &emsp; &emsp; $D=$ { $(x,y): a \leq x \leq b ~ and ~ y_1 (x) \leq y \leq y_2 (x)$ }

&emsp; &emsp; case 8: &emsp; &emsp; $D=$ { $(x,y): x_1 (y) \leq x \leq x_2(y) ~ and ~ y_1 (x) \leq y \leq y_2 (x)$ } 

** Note : case 8 is not implemented in the code cause there is no analytical method to solve such an integral when all limits of x and y depend on each other.

<ins>Step 2:</ins>

&emsp; &emsp; Then decide the series of integration:

&emsp; &emsp; case 1: &emsp; &emsp; $\int_a ^b ( \int_c ^d f(x,y) dy ) dx$

&emsp; &emsp; case 2: &emsp; &emsp; $\int_c ^d ( \int_a ^{x_2 (y)} f(x,y) dx ) dy$

&emsp; &emsp; case 3: &emsp; &emsp; $\int_c ^d ( \int_{x_1 (y)} ^b f(x,y) dx ) dy$

&emsp; &emsp; case 4: &emsp; &emsp; $\int_c ^d ( \int_{x_1 (y)} ^{x_2 (y)} f(x,y) dx ) dy$

&emsp; &emsp; case 5: &emsp; &emsp; $\int_a ^b ( \int_{y_1 (x)} ^d f(x,y) dy ) dx$

&emsp; &emsp; case 6: &emsp; &emsp; $\int_a ^b ( \int_c ^{y_2 (x)} f(x,y) dy ) dx$

&emsp; &emsp; case 7: &emsp; &emsp; $\int_a ^b ( \int_{y_1 (x)} ^{y_2 (x)} f(x,y) dy ) dx$

Then compute the integrals.


Polar coordinates:
------------------

A. For center of transformation $O(0,0)$ :

<ins>Step 1:</ins>

&emsp; &emsp; Replace $x$ with $r \cdot \cos(\theta)$ and $y$ with $r \cdot \sin(\theta)$ :

&emsp; &emsp; $x(r,\theta) = r \cdot \cos(\theta)$ and $y(r,\theta) = r \cdot \sin(\theta)$ .

<ins>Step 2:</ins>

&emsp; &emsp; The new function is :

&emsp; &emsp; $f(r,\theta) = f( x(r,\theta) , y(r,\theta) ) \cdot r$

<ins>Step 3:</ins>

&emsp; &emsp; Compute integral with respect to $r$ and then to $\theta$ .

&emsp; &emsp; $\int_{ \theta _1} ^ {\theta _2} ( \int _{r_1} ^{r_2} f(r,\theta) dr ) d\theta $

B. For center of transformation $K(x_K,y_K)$ :

<ins>Step 1:</ins>

&emsp; &emsp; Replace $x$ with $r \cdot \cos(\theta) + x_K$ and $y$ with $r \cdot \sin(\theta) + y_K$ :

&emsp; &emsp; $x(r,\theta) = r \cdot \cos(\theta) + x_K$ and $y(r,\theta) = r \cdot \sin(\theta) + y_K$ .

<ins>Step 2:</ins>

&emsp; &emsp; The new function is :

&emsp; &emsp; $f(r,\theta) = f( x(r,\theta) , y(r,\theta) ) \cdot r$

<ins>Step 3:</ins>

&emsp; &emsp; Compute integral with respect to $r$ and then to $\theta$ .

&emsp; &emsp; $\int_{ \theta _1} ^ {\theta _2} ( \int _{r_1} ^{r_2} f(r,\theta) dr ) d\theta $


Elliptical Coordinates:
-----------------------

A. For center of transformation $O(0,0)$ :

<ins>Step 1:</ins>

&emsp; &emsp; Replace $x$ with $a \cdot r \cdot \cos(\theta)$ and $y$ with $b \cdot r \cdot \sin(\theta)$ :

&emsp; &emsp; $x(r,\theta) = a \cdot r \cdot \cos(\theta)$ and $y(r,\theta) = b \cdot r \cdot \sin(\theta)$ .

<ins>Step 2:</ins>

&emsp; &emsp; The new function is :

&emsp; &emsp; $f(r,\theta) = f( x(r,\theta) , y(r,\theta) ) \cdot r \cdot a \cdot b$

<ins>Step 3:</ins>

&emsp; &emsp; Compute integral with respect to $r$ and then to $\theta$ .

&emsp; &emsp; $\int_{ \theta _1} ^ {\theta _2} ( \int _{r_1} ^{r_2} f(r,\theta) dr ) d\theta $

B. For center of transformation $K(x_K,y_K)$ :

<ins>Step 1:</ins>

&emsp; &emsp; Replace $x$ with $a \cdot r \cdot \cos(\theta) + x_K$ and $y$ with $b \cdot r \cdot \sin(\theta) + y_K$ :

&emsp; &emsp; $x(r,\theta) = a \cdot r \cdot \cos(\theta) + x_K$ and $y(r,\theta) = b \cdot r \cdot \sin(\theta) + y_K$ .

<ins>Step 2:</ins>

&emsp; &emsp; The new function is :

&emsp; &emsp; $f(r,\theta) = f( x(r,\theta) , y(r,\theta) ) \cdot r \cdot a \cdot b$

<ins>Step 3:</ins>

&emsp; &emsp; Compute integral with respect to $r$ and then to $\theta$ .

&emsp; &emsp; $\int_{ \theta _1} ^ {\theta _2} ( \int _{r_1} ^{r_2} f(r,\theta) dr ) d\theta $



