#!/usr/bin/env python3
"""
uses epsilon-greedy to determine the next action
"""


def epsilon_greedy(Q, state, epsilon):
    """
    uses epsilon-greedy to determine the next action

    Q is a numpy.ndarray containing the q-table
    state is the current state
    epsilon is the epsilon to use for the calculation
    You should sample p with numpy.random.uniformn to determine if your algorithm should explore or exploit
    If exploring, you should pick the next action with numpy.random.randint from all possible actions
    Returns: the next action index
    """
