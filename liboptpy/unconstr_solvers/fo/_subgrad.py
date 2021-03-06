from ... import base_optimizer as _base
import numpy as np

class SubgradientMethod(_base.LineSearchOptimizer):
    def __init__(self, f, subgrad, step_size):
        super().__init__(f, subgrad, step_size)
        self._x_best = None
        self._f_best = np.inf
    
    def get_direction(self, x):
        return -self._grad(x)
    
    def check_convergence(self, tol):
        current_f = self._f(self._x_next)
        if current_f < self._f_best:
            self._x_best = self._x_next
            self._f_best = current_f
        return False
    
    def get_stepsize(self):
        return self._step_size.get_stepsize(self._grad_mem[-1], self._x_current, len(self.convergence))
    
    def _print_info(self):
        pass
    
    def _get_result_x(self):
        return self._x_best