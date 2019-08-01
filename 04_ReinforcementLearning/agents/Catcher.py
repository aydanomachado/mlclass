from ple.games.catcher import Catcher
from ple import PLE
import numpy as np
import random
class RandomAgent:
	def __init__(self, actions):
		self.actions = actions

	def pickAction(self, state, reward):
		return random.choice(self.actions)
'''
State Formate:
{
    'player_x': int,
    'player_vel': float,
    'fruit_x': int,
    'fruit_y': int
}
Actions:
[97, 100, None]
'''

game = Catcher(width=256, height=256, init_lives=3)

p = PLE(game, fps=30, display_screen=True, force_fps=False)
p.init()

agent = RandomAgent(p.getActionSet())
nb_frames = 1000
reward = 0.0

print(game.getGameState())
print(p.getActionSet())

for f in range(nb_frames):
	if p.game_over(): #check if the game is over
		p.reset_game()

	state = game.getGameState()
	action = agent.pickAction(state, reward)
	reward = p.act(action)