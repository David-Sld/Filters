# Filters

# 1 - First order filter

In Laplace domain, the transfer function of a first order filter is given by : 

$$ \frac{Y(s)}{U(s)}  = \frac{1}{\frac{s}{\omega_c} + 1}$$

In the time domain :

$$ \frac{1}{\omega_c} \frac{\mathrm{d}y(t)}{\mathrm{d}t} + y(t) = u(t) $$

In In the discret form

$$\frac{y_{k} - y_{k-1}}{\omega_c T_s} + y_k = u_k$$
$$y_k = \alpha u_k + (1 - \alpha )y_{k-1}$$
with $\alpha = \frac{\omega_c T_e}{ 1 + \omega_c T_e}$


