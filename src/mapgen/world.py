import numpy as np
import matplotlib.pyplot as plt
import defmaps
import models

"""
The world is represented as a 2D numpy array.
"""
class World(object):
    def __init__(self, width=100, height=100, model=None, randstart=False):
        self.width = width
        self.height = height
        self.model = model
        self.time = 0
        self.init_world(randstart)

    @property
    def shape(self):
        return (self.height, self.width)

    def init_world(self, randstart):
        if randstart:
            self.world = np.random.choice((1, 0), self.shape, p=(0.2, 0.8))
        else:
            sqside = int(self.shape[0]/5)
            self.world = defmaps.square(self.shape, sqside)
        self.state = np.zeros(self.shape)
        return self.world

    def __iter__(self):
        return self

    def __next__(self):
        self.time += 1

        self.state = np.copy(self.world)
        self.world = self.model.next_state(self.state, self.time)

        return self.world

    def final(self):
        for state in self:
            continue
        return state

    def display(self, state=None, savepath=None):
        fig, ax = plt.subplots()
        ax.axis('off')
        if state is None:
            mat = ax.matshow(self.world)
        else:
            mat = ax.matshow(state)
        if savepath is None:
            plt.show()
        else:
            plt.savefig(savepath)


if __name__ == "__main__":
    automata = models.CellularAutomata()
    world = World(20, 20, randstart=True, model=automata)
    world.display(world.final())
