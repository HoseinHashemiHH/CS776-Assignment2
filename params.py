
# define the total iterations
class Params_F1():
    
    def __init__(self) -> None:
        
        self.vars_num=3
        # define range for input
        self.bounds = [(-5.12, 5.12)]*self.vars_num
        # define the total iterations
        self.n_iter = 100
        # bits
        self.n_bits = 20
        # define the population size
        self.n_pop = 50
        # crossover rate
        self.r_cross = 0.7
        # mutation rate
        self.r_mut = 0.001
        # ga(djong_f1, n_bits, n_iter, n_pop, r_cross, r_mut)
        
class Params_F2():

    def __init__(self) -> None:
        
        # define range for input
        # define range for input
        self.vars_num=2
        # define range for input
        self.bounds = [(-2.048, 2.048)]*self.vars_num
        # define the total iterations
        self.n_iter = 100
        # bits
        self.n_bits = 20
        # define the population size
        self.n_pop = 50
        # crossover rate
        self.r_cross = 0.7
        # mutation rate
        self.r_mut = 0.001
        # ga(djong_f1, n_bits, n_iter, n_pop, r_cross, r_mut)

class Params_F3():

    def __init__(self) -> None:
        
        # define range for input
        # define range for input
        self.vars_num=5
        # define range for input
        self.bounds = [(-5.12, 5.12)]*self.vars_num
        # define the total iterations
        self.n_iter = 100
        # bits
        self.n_bits = 20
        # define the population size
        self.n_pop = 50
        # crossover rate
        self.r_cross = 0.7
        # mutation rate
        self.r_mut = 0.001
        # ga(djong_f1, n_bits, n_iter, n_pop, r_cross, r_mut)

class Params_F4():

    def __init__(self) -> None:
        
        # define range for input
        # define range for input
        self.vars_num=30
        # define range for input
        self.bounds = [(-1.28,1.28)]*self.vars_num
        # define the total iterations
        self.n_iter = 100
        # bits
        self.n_bits = 20
        # define the population size
        self.n_pop = 50
        # crossover rate
        self.r_cross = 0.7
        # mutation rate
        self.r_mut = 0.001
        # ga(djong_f1, n_bits, n_iter, n_pop, r_cross, r_mut)

class Params_F5():

    def __init__(self) -> None:
        
        # define range for input
        # define range for input
        self.vars_num=50
        # define range for input
        self.bounds = [(-65.536, 65.536)]*self.vars_num
        self.bounds_f5 = []
        # define the total iterations
        self.n_iter = 100
        # bits
        self.n_bits = 20
        # define the population size
        self.n_pop = 50
        # crossover rate
        self.r_cross = 0.7
        # mutation rate
        self.r_mut = 0.001
        # ga(djong_f1, n_bits, n_iter, n_pop, r_cross, r_mut)
    
class CHC_Params():
        def __init__(self) -> None:
            self.n_iter = 200
            # bits
            self.n_bits = 20
            # define the population size
            self.n_pop = 50
            # crossover rate
            self.r_cross = 0.95
            # mutation rate
            self.r_mut = 0.05