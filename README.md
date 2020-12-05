# Python-Runge-Kutta
This repository contains a Time saving Runge-Kutta ODE Solver in Python.
This ODE solver allows one to solve multiple ODEs by selecting different Runge-Kutta orders.

<b>RK_ODE_Solver</b> class object contains <b>calc(y, ode, xs, xf, dx, ord)</b> method object that conducts the calculation.
### Parameters:
<b>y</b>: <b><i> array_like </i></b> 

The dependent function(s).

<b>ode</b>: <b><i> callable </i></b>

The model function, ode(y, x=None) It must take the independent variable as the first argument.

<b>xs</b>: <b>float</b>

The starting point or initial vaue of the independent variable.

<b>xf</b>: <b>float</b>

The final point (value) of the independent variable.

<b>dx</b>: <b>float</b>

incerement for for the independent variable from xs to xf

<b>ord</b>: <b>{1, 4, 5, 6}, optional</b> 

Runge-Kutta Order. Default is {4}

