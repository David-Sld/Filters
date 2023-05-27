# Filters

# 1 - First order filter

In Laplace domain, the transfer function of a first order filter is given by : 

$$ \frac{Y(s)}{U(s)}  = \frac{1}{\frac{s}{w} + 1}$$

In the time domain :

$$\frac{\mathrm{d}y(t)}{\mathrm{d}t} * \frac{1}{w} + y(t) = u(t) $$

In In the discret form

$$\frac{y_{k} - y_{k-1}}{T_s  } * \frac{1}{w} + y_k = u_k$$
$$y_k = \alpha u_k + (1 - \alpha )y_{k-1}$$
with $\alpha = \frac{T_e}{ \frac{1}{w} + T_e}$
    $\alpha = \frac{w T_e}{ 1 + w T_e}$


