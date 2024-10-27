# Reinforcement Learning Repository

Welcome to my **Reinforcement Learning Repository**!<br>
This repository contains a variety of projects organized under different topics in reinforcement learning and data processing. Each main directory (`pipeline`, `reinforcement_learning`) groups related projects and concepts for easy access.

## Table of Contents
- [Project Overview](#project-overview)
- [Projects](#projects)
  - [pipeline](#pipeline)
    - [apis](#apis)
    - [databases](#databases)
    - [pandas](#pandas)
  - [reinforcement_learning](#reinforcement_learning)
    - [deep_q_learning](#deep_q_learning)
    - [policy_gradients](#policy_gradients)
    - [q_learning](#q_learning)
    - [temporal_difference](#temporal_difference)

---

## Project Overview

This repository features projects that implement reinforcement learning techniques, data processing, and data collection methodologies. Each project leverages frameworks such as OpenAI Gym, Keras, and Pandas to explore various aspects of reinforcement learning and data manipulation.

---

## Projects

### [pipeline](pipeline)

#### [apis](pipeline/apis)
This section focuses on interacting with APIs to retrieve and display data. The projects here involve API calls to gather information about spaceships, planets, and rocket launches using the SWAPI and SpaceX APIs. It also includes tasks for fetching data, handling pagination, and formatting output.

#### [databases](pipeline/databases)
This section covers the creation and management of databases. Projects here involve tasks such as creating tables, inserting data, and performing retrieval and aggregation operations in MySQL and MongoDB.

#### [pandas](pipeline/pandas)
This section utilizes the pandas library for data manipulation and analysis. Projects include creating DataFrames from various sources, renaming columns, handling missing values, concatenating DataFrames, and visualizing data.

---

### [reinforcement_learning](reinforcement_learning)

#### [deep_q_learning](reinforcement_learning/deep_q_learning)
This section contains projects that create Deep Q-Learning agents. Notably, it includes a project that trains a DQN agent to play Atari's Breakout using Keras. The project covers the fundamentals of Deep Q-Learning, policy networks, and agent training.

#### [policy_gradients](reinforcement_learning/policy_gradients)
This section implements policy gradient methods for reinforcement learning. Projects here focus on training agents in environments like CartPole, covering policy function computation and Monte Carlo policy gradient calculations.

#### [q_learning](reinforcement_learning/q_learning)
This section features traditional Q-Learning projects. The primary project creates a reinforcement learning agent that navigates the Frozen Lake environment using Q-Learning. It includes environment setup, Q-table initialization, and agent training.

#### [temporal_difference](reinforcement_learning/temporal_difference)
This section explores temporal difference learning methods. Projects include implementations of Monte Carlo methods, TD(λ), and SARSA(λ) for solving the Frozen Lake environment, focusing on value estimation and updating methods.

---

Feel free to explore each section by clicking the project names above to access their respective directories and dive deeper into the code and methodologies used.
