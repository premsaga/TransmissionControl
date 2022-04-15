import argparse
parser = argparse.ArgumentParser()
parser.add_argument("n_agents", type=int)
parser.add_argument("n_actions", type=int)
parser.add_argument("threshold", help="How many agents can successfully transmit at the same time", type=int)
parser.add_argument("feature_history", help="Use information from the past x steps as features", type=int)
args = parser.parse_args()

print(args)
print(dir(args))
print(args.n_agents, type(args.n_agents))
