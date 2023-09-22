from numpy import array, reshape, zeros, eye
"""
g/h filter (also known as alpha/beta filter) is a filter that assume system state X is
X = [x; x_dot]  wioth x_dot is constant. It also assumes measurement to b x.
The prediction always state that 
"""

class g_h_filter:

    def __init__(self, X0 : list, g : float, h : float):
        self.N = int(len(X0)/2.0)
        self.X = reshape(X0, (len(X0), 1));
        self.residuals = zeros((self.N, 1))
        self.g = g
        self.h = h
        

    def Predict(self, dt : float):
 
        A = array([[1.0 if ((j + self.N) == i) else 0.0 for i in range(2 * self.N)] \
                      for j in range(2 * self.N)])
        
        self.X = (eye(2 * self.N) + dt * A) @ self.X
        return self.X


    def Update(self, measurement : list, dt : float):
        mes = reshape(measurement, (self.N, 1))
        self.residuals = mes[0:self.N] -  self.X[0:self.N]
        # Speed update
        self.X[self.N:] = self.X[self.N:] + self.g / dt * self.residuals
        # State update
        self.X[0:self.N] += self.h * self.residuals
        return self.X

    def RunEpoch(self, dt : float, measurement : list):
        self.predict(dt)
        self.update(measurement, dt)
        
        
