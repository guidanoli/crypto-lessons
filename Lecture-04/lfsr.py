
def get_initial_ff_state(m):
    """Generate a list of flip flop states with first flip flop
    on and the rest off.

    Parameters
    ----------
    m : int
        Number of flip flops

    Returns
    -------
    list
        List of flip flop states with size m

    """
    return [True] + [False] * (m-1)

def get_p_states(m):
    """Generate a list with switch states according to user input

    Parameters
    ----------
    m : int
        Number of switches

    Returns
    -------
    list
        List of states with size m

    """
    p_lst = list()
    for i in range(m):
        p_state = input("p[{}] = ".format(i+1)) != "0"
        p_lst.append(p_state)
    return p_lst

class LFSR:
    ff_states = None
    p_states = None
    m = 0

    def __init__(self, ff, p, m):
        """Constructs a LSFR object.

        Parameters
        ----------
        ff : list
            List of all flip flop states (boolean).
        p : list
            List of all switches states (boolean).
        m : int
            # of flip flops and switches.

        Returns
        -------
        LSFR
            Linear Feedback Shift Registers object.

        """
        self.ff_states = ff
        self.p_states = p
        self.m = m

    def get_current_s(self):
        """Get s_i value

        Returns
        -------
        int
            s_i value

        """
        return 1 if self.ff_states[0] else 0

    def update(self):
        s_m = False
        for i in range(m):
            res = self.p_states[i] and self.ff_states[i]    # and / mod2 add
            s_m = s_m != res        # xor / mod2 mult
        self.ff_states = self.ff_states[1:] + [s_m]

m_str = input("# of flip-flops = ")
assert m_str.isnumeric(), "# of flip-flops must be a natural number"
m = int(m_str)
assert m > 0, "# of flip-flops must be positive"
ff_lst = get_initial_ff_state(m)
p_lst = get_p_states(m)
lfsr = LFSR(ff_lst, p_lst, m)
rep_str = input("# of repetitions = ")
assert rep_str.isnumeric(), "# of repetitions must be a natural number"
rep = int(rep_str)
assert rep > 0, "# of repetitions must be positive"
for i in range(rep):
    print("s_{} = {}".format(i, lfsr.get_current_s()))
    lfsr.update()
