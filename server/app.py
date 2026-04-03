from fastapi import FastAPI
from env.environment import CloudKitchenEnv
from env.models import Action
import uvicorn

app = FastAPI()
env = CloudKitchenEnv()


@app.post("/reset")
def reset():
    obs = env.reset()
    return obs.model_dump()


@app.post("/step")
def step(action: dict):
    act = Action(**action)
    obs, reward, done, info = env.step(act)

    return {
        "observation": obs.model_dump(),
        "reward": reward.value,
        "done": done,
        "info": info
    }


@app.get("/state")
def state():
    return env.state().model_dump()


@app.get("/")
def home():
    return {"message": "Cloud Kitchen Env running 🚀"}


def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)



if __name__ == "__main__":
    main()