from AgentBase import Agent
from random import randrange
import numpy as np

class CsmaAgent(Agent):
    def __init__(self, wait_for_idle=False):
        """
        Arugments:
            - wait_for_idle [Boolean]: If true, requires a spectrum-sensed reading
            of 0 before transmitting.
        """
        self.wait_for_idle = wait_for_idle

        # Backoff timer will be set as an integer in [0, self.backoff_upper_bound)
        self.backoff_timer = 0
        self.backoff_upper_bound = 2 # non-inclusive upper bound
        

    def choose_action(self, state):
        """ 
        Very ad hoc and dependent on the feature space.
        Follows an exponential backoff strategy.

        Returns:
            - 0 --> do not transmit on the next step
            - 1 -->  transmit on the next step
       """
       
        state = np.squeeze(state)
        #print(state.shape, state)
        # Did the agent transmit?
        did_transmit = state[-3]
        if did_transmit == 1:
            # Was the transmission successful? 
            n_successful_transmissions = state[-4] 
            if n_successful_transmissions > 0:
                # Successful --> reset self.backoff_timer and self.backoff_upper_bound 
                self.backoff_timer = 0
                self.backoff_upper_bound = 2 
            else:
                # Unsuccessful --> Increase the self.backoff_upper_bound and set a new self.backoff_timer  
                self.backoff_upper_bound *= 2
                self.backoff_timer = randrange(self.backoff_upper_bound)

	    # Check if we're in a backoff phase
        if self.backoff_timer > 0:
            self.backoff_timer -= 1
            return 0

        # Transmit procedure: if wait_for_idle check interference-sensed
        spectrum_sensed = state[-2]
        if self.wait_for_idle:
            if did_transmit or (spectrum_sensed != 0):
                return 0

        return 1

    def remember(self, state, action, reward, next_state, done):
        """ Store trajectory in the agent's experience replay memory """
        pass

    def learn(self):
        """ Train the agent """
        pass
