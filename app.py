from fastapi import FastAPI, HTTPException
from env.environment import CloudKitchenEnv
from env.models import Action

app = FastAPI()

env = CloudKitchenEnv()


@app.get("/")
def home():
    return {"message": "Cloud Kitchen Env running 🚀"}


@app.post("/reset")
def reset():
    try:
        obs = env.reset()
        return obs.model_dump()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/step")
def step(action: dict):
    try:
        act = Action(**action)

        obs, reward, done, info = env.step(act)

        return {
            "observation": obs.model_dump(),
            "reward": float(reward.value),
            "done": done,
            "info": info
        }

    except Exception as e:
        
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/state")
def state():
    try:
        return env.state().model_dump()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

