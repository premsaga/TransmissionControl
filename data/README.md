# TransmissionControl

Data:
- run1: Before some bug fixes to features
- run2: 2 agents, 3 actions, threshold 1. After fixing features. Source rate set to 2.
- run3: 2 agents, 3 actions, threshold 1. Fix to make sure buffer cannot exced max buffer. Source rate chhanged from 2 --> 1.
- run4: Same as run 3, but with transmit_and_sense turned to false
- run5: 4 agents, 5 actions, history 1, transmit_and_sense=False, with newer feature history code (new feature history code may be bugged)
- run6: 4 agents, 5 actions, history 1, transmit_and_sense=True, with older feature history code 
- run7: Same as run6, but with transmit_and_sense=False
- run8: Same as run7 but with more steps 10,000 -> 20,000
- run9: Same as run7, 20k steps
- run10: Same as run8, 10k steps
- run11: 4, agents, 5 actions, history = 3, transmit_and_sense=false (testing feature histories)
- run12: Same as runs 8 and 10, 10k steps, history=1

