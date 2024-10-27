# Frozen Lake Q-Learning Agent

## Table of Contents
- [Project Overview](#project-overview)
- [What is Q-Learning?](#what-is-q-learning)
- [Frozen Lake Environment](#frozen-lake-environment)
- [Agent Components](#agent-components)
- [Training the Agent](#training-the-agent)
- [Testing the Agent](#testing-the-agent)
- [Dependencies](#dependencies)
- [References](#references)

---

## Project Overview

This project demonstrates the implementation of a **Q-learning agent** to solve OpenAI Gym's **FrozenLake environment**, a grid-based world where an agent learns to navigate a slippery, icy surface to reach a goal while avoiding holes. The agent is trained over numerous episodes, refining its decisions to maximize rewards and avoid pitfalls.

Key concepts implemented:
- Q-table initialization and updates using Q-learning.
- Epsilon-greedy strategy for balancing exploration and exploitation.
- Training and testing of the agent’s learned policy.
  
---

## What is Q-Learning?

**Q-Learning** is a **model-free reinforcement learning** algorithm used to find an optimal policy in environments modeled as Markov decision processes (MDPs). In Q-learning:
- The agent learns an **action-value function**, represented as a Q-table, which stores expected rewards for each state-action pair.
- This Q-table is updated iteratively using the formula:

    ```
    Q(s, a) = Q(s, a) + α * [r + γ * max(Q(s', a')) - Q(s, a)]
    ```

    where:
    - `s` is the current state,
    - `a` is the action taken,
    - `r` is the reward received,
    - `s'` is the next state,
    - `a'` is the next action,
    - `α` is the learning rate, and
    - `γ` is the discount factor, which balances immediate and future rewards.

This Q-learning algorithm enables the agent to learn an optimal policy by interacting with the environment, even without knowledge of the environment’s internal dynamics.

---

## Frozen Lake Environment

The **FrozenLake environment** is a grid world where each cell represents either:
- **Start (S)**: The initial position of the agent.
- **Goal (G)**: The target position the agent must reach.
- **Frozen surface (F)**: Safe cells the agent can walk on.
- **Hole (H)**: Dangerous cells that cause the agent to fail if stepped on.

In the **slippery** setting, the environment introduces randomness by occasionally moving the agent in unintended directions, adding a layer of complexity to the task.

---

## Agent Components

### 1. Load the Environment
The `load_environment` function initializes the FrozenLake environment from Gym, allowing custom map settings and adjustable "slippery" conditions to vary the challenge.

### 2. Initialize Q-Table
The Q-table is a 2D array initialized with zeros. Each row represents a state in the environment, and each column represents an action the agent can take. Over training, this table is updated to reflect the agent’s learned policy.

### 3. Epsilon-Greedy Action Selection
The **epsilon-greedy** strategy balances **exploration** (choosing random actions) and **exploitation** (choosing the best-known action):
- With probability `ε`, a random action is chosen.
- With probability `1 - ε`, the action with the highest Q-value for the current state is selected.

This ensures the agent doesn’t get stuck in local optima and continues to explore the environment.

### 4. Q-Learning Training Process
The `train` function iterates over a set number of episodes:
- The agent observes its current state and selects an action using the epsilon-greedy policy.
- After taking the action, it receives a reward and transitions to a new state.
- The Q-value for the state-action pair is updated according to the Q-learning formula.
- This process is repeated until the agent reaches the goal or falls into a hole.

The result is an updated Q-table representing the learned policy, where the agent has a higher chance of choosing actions that lead to the goal.

---

## Training the Agent

The `train` function runs the Q-learning algorithm over a specified number of episodes, adjusting the Q-table at each step to improve the policy. The agent’s training progress is logged, showing the total rewards achieved over time. The rewards indicate how well the agent has learned to navigate the environment.

## Testing the Agent

The `play` function is used to test the trained agent by navigating the Frozen Lake environment with the learned Q-table. Here, the agent follows the optimal policy by selecting actions with the highest Q-value for each state.

---

## Dependencies

To run this project, you’ll need:
- Python 3.x
- Gymnasium (for FrozenLake environment)
- NumPy (for handling the Q-table)

Install the required packages:
```bash
pip install gymnasium numpy
```

## References
gymnasium frozen lake documentation: https://gymnasium.farama.org/environments/toy_text/frozen_lake/

