class Model(object):
    def next_state(self, state, time, *args, **kwargs):
        raise NotImplementedError()

class CellularAutomata(Model):
    def _neighbors(self, state, idx, jdx):
        return [
            state[idx, jdx],
            state[(idx-1)%state.shape[0], jdx],
            state[idx, (jdx+1)%state.shape[1]],
            state[(idx+1)%state.shape[0], jdx],
            state[idx, (jdx-1)%state.shape[1]]
        ]

    def odd_parity(self, array):
        return sum(array) % 2

    def next_state(self, state, time, *args, **kwargs):
        if state.shape[0] < time:
            raise StopIteration
        for row in range(state.shape[0]):
            for col in range(state.shape[1]):
                if self.odd_parity(self._neighbors(state, row, col)):
                    state[row, col] = 1
                else:
                    state[row, col] = 0
        return state