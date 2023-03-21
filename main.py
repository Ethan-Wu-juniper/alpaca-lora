from fastapi import FastAPI
from generate import initialized
import pydantic

class Input(pydantic.BaseModel):
    prompts: str
    temperature: float = 0.8
    top_p: float = 0.95

class Output(pydantic.BaseModel):
    results: str

app = FastAPI()


@app.post("/prompt")
def prompt(_input: Input) -> Output:
    results = initialized(
        _input.prompts,
        temperature=_input.temperature,
        top_p=_input.top_p,
    )
    return Output(results=results)