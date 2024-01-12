#!/usr/bin/env python3
"""
has a trained agent play an episode
"""


def play(env, Q, max_steps=100):
    """
    env is the FrozenLakeEnv instance
    Q is a numpy.ndarray containing the Q-table
    max_steps is the maximum number of steps in the episode
    Each state of the board should be displayed via the console
    You should always exploit the Q-table
    Returns: the total rewards for the episode
    """
