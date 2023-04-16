# Filters

# 1 - First order filter

In Laplace domain, the transfer function of a first order filter is given by : 

$$ \frac{Y(s)}{U(s)}  = \frac{1}{\tau s + 1}$$

In the time domain :

$$\frac{\mathrm{d}y(t)}{\mathrm{d}t} \tau + y(t) = u(t) $$

In In the discret form

$$\frac{y_{k} - y_{k-1}}{T_s  } \tau + y_k = u_k$$
$$y_k = \alpha u_k - (1 - \alpha )y_{k-1}$$
with $\alpha = \frac{T_e}{\tau + T_e}$


