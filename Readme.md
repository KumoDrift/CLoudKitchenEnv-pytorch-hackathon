---
title: Cloud Kitchen Environment
emoji: 🍳
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
---

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

## 🧠 Environment Design

The environment follows a standard **OpenEnv-style API** implemented as a FastAPI app.

### Core Endpoints

- `POST /reset` → Initializes the environment and returns the initial observation
- `POST /step` → Executes an agent action and returns observation, reward, done, info
- `GET /state` → Returns the current environment state
- `GET /` → Health check (returns "Cloud Kitchen Env running 🚀")

### Core Methods (Backend)

- `reset()` → Initializes environment
- `step(action)` → Executes agent action
- `state()` → Returns current observation

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

## 🔗 Base URL

https://ichi-goat7-cloud-kitchen-env.hf.space

---

## 🔄 1. Reset Environment

### Endpoint

POST /reset

### Description

Resets the environment to the initial state.

### Request

No body required.

### Example (PowerShell)

    Invoke-RestMethod `
    -Uri "https://ichi-goat7-cloud-kitchen-env.hf.space/reset" `
    -Method POST

### Example (curl)

    curl -X POST https://ichi-goat7-cloud-kitchen-env.hf.space/reset

### Response

    {
      "current_time": 0,
      "orders": [...],
      "slots": [...]
    }

---

## ⚡ 2. Take a Step

### Endpoint

POST /step

### Description

Executes one environment step using the provided action.

### Request Payload

    {
      "assignments": [
        {
          "slot_id": 1,
          "order_id": 1
        }
      ]
    }

### Example (PowerShell)

    Invoke-RestMethod `
    -Uri "https://ichi-goat7-cloud-kitchen-env.hf.space/step" `
    -Method POST `
    -Body '{"assignments":[{"slot_id":1,"order_id":1}]}' `
    -ContentType "application/json"

### Example (curl)

    curl -X POST https://ichi-goat7-cloud-kitchen-env.hf.space/step \
    -H "Content-Type: application/json" \
    -d '{"assignments":[{"slot_id":1,"order_id":1}]}'

### Response

    {
      "observation": {
        "current_time": 1,
        "orders": [...],
        "slots": [...]
      },
      "reward": 0.0,
      "done": false,
      "info": {
        "events": []
      }
    }

---

## 📊 3. Get Current State

### Endpoint

GET /state

### Description

Returns the current environment state without modifying it.

### Example (PowerShell)

    Invoke-RestMethod `
    -Uri "https://ichi-goat7-cloud-kitchen-env.hf.space/state"

### Example (curl)

    curl https://ichi-goat7-cloud-kitchen-env.hf.space/state

### Response

    {
      "current_time": 0,
      "orders": [...],
      "slots": [...]
    }

## ✅ Action Format Summary

    {
      "assignments": [
        { "slot_id": int, "order_id": int }
      ]
    }

---

## 🏁 Example Workflow

1. POST /reset
2. POST /step (assign orders)
3. Repeat `/step` until `"done": true`

---

## 🎯 Motivation

Unlike toy problems or games, this environment models a **real operational challenge** faced by cloud kitchens:

> "How do you prioritize and schedule orders when resources are limited and deadlines matter?"

This introduces real-world complexities like:

- Trade-offs between **speed vs value**
- Resource contention (limited slots)
- Time-sensitive decision making

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

## ▶️ Run Inference

```bash
python inference.py
```

---

## 🐳 Docker Support

Build and run:

```bash
docker build -t cloud-kitchen-env .
docker run -p 7860:7860 cloud-kitchen-env
```

---

## 👨‍💻 Author

**KumoDrift**  
Cloud Kitchen RL Environment Project
