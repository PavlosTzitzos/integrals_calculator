Double Integrals:
-----------------
Definition: $\int \int _D f(x,y) dx dy$

Cartesian Coordinates:
----------------------

Initally:

Focus only to make the double integral into simple integrals of one variable.

Step 1:

If $D$ is known then choose the apropriate case:

case 1: $D=$ { $(x,y\): a \leq x \leq b ~ and ~ c \leq y \leq d$ }

case 2: $D=$ { $(x,y): a \leq x \leq x_2 (y) ~ and ~ c \leq y \leq d$ }

case 3: $D=$ { $(x,y): x_1 (y) \leq x \leq b ~ and ~ c \leq y \leq d$ }

case 4: $D=$ { $(x,y): x_1 (y) \leq x \leq x_2 (y) ~ and ~ c \leq y \leq d$ }

case 5: $D=$ { $(x,y): a \leq x \leq b ~ and ~ y_1 (x) \leq y \leq d$ }

case 6: $D=$ { $(x,y): a \leq x \leq b ~ and ~ c \leq y \leq y_2 (x)$ }

case 7: $D=$ { $(x,y): a \leq x \leq b ~ and ~ y_1 (x) \leq y \leq y_2 (x)$ }

case 8: $D=$ { $(x,y): x_1 (y) \leq x \leq x_2(y) ~ and ~ y_1 (x) \leq y \leq y_2 (x)$ } 

** Note : case 8 is not implemented in the code cause there is no analytical method to solve such an integral when all limits of x and y depend on each other.

Step 2:

Then decide the series of integration:

case 1: $\int_a ^b ( \int_c ^d f(x,y) dy ) dx$

case 2: $\int_c ^d ( \int_a ^{x_2 (y)} f(x,y) dx ) dy$

case 3: $\int_c ^d ( \int_{x_1 (y)} ^b f(x,y) dx ) dy$

case 4: $\int_c ^d ( \int_{x_1 (y)} ^{x_2 (y)} f(x,y) dx ) dy$

case 5: $\int_a ^b ( \int_{y_1 (x)} ^d f(x,y) dy ) dx$

case 6: $\int_a ^b ( \int_c ^{y_2 (x)} f(x,y) dy ) dx$

case 7: $\int_a ^b ( \int_{y_1 (x)} ^{y_2 (x)} f(x,y) dy ) dx$

Then compute the integrals.


Polar coordinates:
------------------

For center of transformation $O(0,0)$ :

Step 1:

Replace $x$ with $r \cdot \cos(\theta)$ and $y$ with $r \cdot \sin(\theta)$ :

$x(r,\theta) = r \cdot \cos(\theta)$ and $y(r,\theta) = r \cdot \sin(\theta)$ .

Step 2:

The new function is :

$f(r,\theta) = f( x(r,\theta) , y(r,\theta) ) \cdot r$

Step 3:

Compute integral with respect to $r$ and then to $\theta$ .

$\int_{ \theta _1} ^ {\theta _2} ( \int _{r_1} ^{r_2} f(r,\theta) dr ) d\theta $

For center of transformation $K(x_K,y_K)$ :

Step 1:

Replace $x$ with $r \cdot \cos(\theta) + x_K$ and $y$ with $r \cdot \sin(\theta) + y_K$ :

$x(r,\theta) = r \cdot \cos(\theta) + x_K$ and $y(r,\theta) = r \cdot \sin(\theta) + y_K$ .

Step 2:

The new function is :

$f(r,\theta) = f( x(r,\theta) , y(r,\theta) ) \cdot r$

Step 3:

Compute integral with respect to $r$ and then to $\theta$ .

$\int_{ \theta _1} ^ {\theta _2} ( \int _{r_1} ^{r_2} f(r,\theta) dr ) d\theta $

Elliptical Coordinates:
-----------------------

For center of transformation $O(0,0)$ :

Step 1:

Replace $x$ with $a \cdot r \cdot \cos(\theta)$ and $y$ with $b \cdot r \cdot \sin(\theta)$ :

$x(r,\theta) = a \cdot r \cdot \cos(\theta)$ and $y(r,\theta) = b \cdot r \cdot \sin(\theta)$ .

Step 2:

The new function is :

$f(r,\theta) = f( x(r,\theta) , y(r,\theta) ) \cdot r \cdot a \cdot b$

Step 3:

Compute integral with respect to $r$ and then to $\theta$ .

$\int_{ \theta _1} ^ {\theta _2} ( \int _{r_1} ^{r_2} f(r,\theta) dr ) d\theta $


For center of transformation $K(x_K,y_K)$ :

Step 1:

Replace $x$ with $a \cdot r \cdot \cos(\theta) + x_K$ and $y$ with $b \cdot r \cdot \sin(\theta) + y_K$ :

$x(r,\theta) = a \cdot r \cdot \cos(\theta) + x_K$ and $y(r,\theta) = b \cdot r \cdot \sin(\theta) + y_K$ .

Step 2:

The new function is :

$f(r,\theta) = f( x(r,\theta) , y(r,\theta) ) \cdot r \cdot a \cdot b$

Step 3:

Compute integral with respect to $r$ and then to $\theta$ .

$\int_{ \theta _1} ^ {\theta _2} ( \int _{r_1} ^{r_2} f(r,\theta) dr ) d\theta $



