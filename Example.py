from numpy import exp as exp
from numpy import array as array

class Coefficients(object):
    def __init__(self):
        self.RK_1 = {'wg': [1]}
        self.RK_1['alf'] = self.RK_1['wg']

        self.RK_4 = {'wg': [1., .5, 1. / 6., 1. / 24]}
        _lst = self.RK_4['wg']
        self.RK_4['alf'] = [
            _lst[3] / _lst[2],
            _lst[2] / _lst[1],
            _lst[1] / _lst[0],
            _lst[0]
        ]

        self.RK_5 = {'wg': [1., .5, .165250353664, .039372585984, .007149096448]}
        _lst = self.RK_5['wg']
        self.RK_5['alf'] = [
            _lst[4] / _lst[3],
            _lst[3] / _lst[2],
            _lst[2] / _lst[1],
            _lst[1] / _lst[0],
            _lst[0]
        ]

        self.RK_6 = {'wg': [1., .5, .165919771368, .040919732041, .007555704391, .000891421261]}
        _lst = self.RK_6['wg']
        self.RK_6['alf'] = [
            _lst[5] / _lst[4],
            _lst[4] / _lst[3],
            _lst[3] / _lst[2],
            _lst[2] / _lst[1],
            _lst[1] / _lst[0],
            _lst[0]
        ]

        self.RK = {1: self.RK_1, 4: self.RK_4, 5: self.RK_5, 6: self.RK_6}


class RK_ODE_Solver(Coefficients):
    def __init__(self):
        # ord: Runge Kutta Order
        super().__init__()


    def calc(self, y, ode, xs, xf, dx, ord=4):
        if ord not in [1, 4, 5, 6]:
            print('Runge Kutta Order should be 1, 4, 5, 6')
            exit()
        self.ord = ord
        self.alf = self.RK[ord]['alf']
        self.ode = ode
        self.xs = xs
        self.xf = xf
        self.dx = dx
        self.__n = round((xf-xs)/dx)
        self.dx = (xf-xs)/self.__n
        self.y = array(y)


        for i in range(self.__n):
            self.__yconst = self.y
            for j in range(self.ord):
                self.__dy_dx = array(self.ode(self.y))
                self.y = self.__yconst+self.alf[j]*self.dx*self.__dy_dx
        return self.y



if __name__ == '__main__':

    '''
    Example
    
    Equations:
    y1(t) = t
    y2(t) = e^t
    
    ODEs:
    dy1/dt = 1
    dy2/dt = e^t
    
    Initial Cond:
    at t=0
    y1(0) = 0
    y2(0) = 1
    
    at t=2
    y1(2) = ??
    y2(2) = ??
    '''


    def ode(y, x=None):
        '''
        y(1) = t --> dy / dt = 1
        y(2) = e ^ t --> dy / dt = e ^ t
        '''
        # f: dy/dx
        f = [None]*2
        f[0] = 1.0
        f[1] = exp(y[0])
        f = [f[0], f[1]]
        return f

    xs = 0 # --> t = 0
    xf = 2 # --> t = 2
    dx = 0.01 # --> increment for t
    y = [0, 1] # ---> initial conditions


    cons = RK_ODE_Solver()

    print(list(cons.calc(y, ode, xs, xf, dx)))
