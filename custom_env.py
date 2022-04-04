import gym
import numpy as np

class threshold_env(gym.Env):
    def __init__(self, n_agents, threshold, n_steps=1e4, buffers=None, max_buffers=None,
               buffer_intervals=None):
        self.observation_space = gym.spaces.Box(low=np.NINF, high=np.inf, shape=[3*n_agents])
        self.action_space = gym.spaces.Box(low=np.NINF, high=np.inf, shape=[n_agents])
        self.n_agents = n_agents
        self.threshold = threshold
        self.n_steps = n_steps
        self.current_step = 0
        self.buffers = buffers if buffers != None else [1]*n_agents
        self.max_buffers = max_buffers if buffers !=None else [100]*n_agents
        self.buffer_intervals = buffer_intervals if buffer_intervals != None else [1]*n_agents

    def step(self, actions):
        """
        Observation space:
            - Did transmit: {0=no, 1=yes}
            - Transmission successful: {0=no, 1=yes}
            - Interference-sensed: Ratio # of other transmissions / # of agents
            - Buffer: Ratio of buffer / max_buffer, [0, 1]
        """
        # Increment step
        self.current_step += 1

        n_transmissions = actions.count(1)
        if n_transmissions <= self.threshold:
            transmissions_successful = True
        else:
            transmissions_successful = False

        # Get reward, observation, and decrement and/or increment buffers
        obs = []
        rewards = []
        for i in range(self.n_agents):
            did_transmit = (actions[i] == 1)
            interference_sensed = n_transmissions / self.n_agents
            buffer_ratio = self.buffers[i] / self.max_buffers[i]


            # Get reward
            if actions[i] == 1:
                if transmissions_successful:
                    # Decrement buffer
                    self.buffers[i] -= 1

                    if self.buffers[i] < 0:
                        raise ValueError("Buffers should not be negative")

                    reward = 1 # successful transmission

                else:
                    reward = -1 # unsuccessful transmission
            elif actions[i] == 0:
                reward = 0 # action = 0, no transmission
            else:
                print("Is this ever used?") # Delete this later
                reward = 0

            rewards.append(reward)

            # Increment buffers
            if self.current_step % self.buffer_intervals[i] == 0:
                self.buffers[i] += 1

            # Get observation
            obs.append([int(did_transmit), int(transmissions_successful), interference_sensed, buffer_ratio])

        # Get "done"
        if self.current_step == self.n_steps:
            done = True
        else:
            done = False

        # Get info
        info = []


        return obs, rewards, done, info

    def reset(self):
        self.current_step = 0
        self.buffers = [0] * self.n_agents
        starting_obs = [0] * (3 * self.n_agents)
        return starting_obs
