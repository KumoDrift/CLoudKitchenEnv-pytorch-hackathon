# 🍳 Cloud Kitchen Scheduling Environment (OpenEnv)

## 🚀 Overview

This project implements a **real-world reinforcement learning environment** simulating a cloud kitchen operation.

An AI agent must intelligently **schedule incoming food orders** to limited cooking slots (stoves), while managing:

- ⏱️ Cooking time
- 📦 Order deadlines
- 🔥 Limited kitchen resources
- 💰 Revenue optimization

The goal is to **maximize total reward** by completing high-value orders on time while avoiding inefficiencies.

---

## 🎯 Motivation

Unlike toy problems or games, this environment models a **real operational challenge** faced by cloud kitchens:

> "How do you prioritize and schedule orders when resources are limited and deadlines matter?"

This introduces real-world complexities like:

- Trade-offs between **speed vs value**
- Resource contention (limited slots)
- Time-sensitive decision making

---

## 🧠 Environment Design

The environment follows a standard **OpenEnv-style API**:

### Core Methods

- `reset()` → Initializes environment
- `step(action)` → Executes agent action
- `state()` → Returns current observation

---

## 📥 Observation Space

Each step returns:

- `current_time` → Current timestep
- `orders` → List of pending orders
- `slots` → Current cooking slot status

---

## 🎮 Action Space

The agent provides assignments of **order_id → slot_id**

### Example

```python
Action(assignments=[
    Assignment(slot_id=1, order_id=2)
])
```

---

## 🔄 Design Note

Initially, the environment supported explicit manual assignment of orders to slots.

In the current version, the baseline agent automates this process using a scheduling strategy:

- When a slot becomes free, the agent automatically selects an order
- Orders are chosen based on **Earliest Deadline First (EDF)**

👉 This reflects a more realistic system where decisions are made dynamically rather than manually.

---

## 🏆 Reward Function

The reward system reflects operational efficiency:

### ✅ Positive Rewards

- Full reward → Order completed before deadline
- Partial reward → Order completed slightly late

### ❌ Penalties

- Late completion → Reduced or negative reward
- Idle cooking slot → Penalty (unused resource)

👉 This encourages the agent to **keep slots busy** and **prioritize timely deliveries**

---

## 📊 Tasks & Difficulty Levels

We define 3 tasks with increasing difficulty:

| Task      | Description                                   |
| --------- | --------------------------------------------- |
| 🟢 Easy   | Sufficient resources, relaxed constraints     |
| 🟡 Medium | Tighter deadlines, fewer slots                |
| 🔴 Hard   | High pressure, extra orders, strict deadlines |

---

## 📈 Baseline Results

- Easy → ~0.77
- Medium → ~0.32
- Hard → ~0.12

### Interpretation

- Agent performs well in simple settings
- Performance drops under constraints
- Demonstrates increasing task complexity

---

## ✅ Key Features

- ✔ Real-world task (cloud kitchen scheduling)
- ✔ OpenEnv-compatible API
- ✔ Typed models using Pydantic
- ✔ Multi-task evaluation system
- ✔ Continuous reward shaping
- ✔ Reproducible baseline results
- ✔ Dockerized for deployment

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/KumoDrift/CLoudKitchenEnv-pytorch-hackathon
cd cloud-kitchen-env
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Baseline

```bash
python baseline.py
```

---

## 🐳 Docker Support

Build and run:

```bash
docker build -t cloud-kitchen-env .
docker run cloud-kitchen-env
```

---

## 👨‍💻 Author

**KumoDrift**  
Cloud Kitchen RL Environment Project
