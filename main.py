from fastapi import FastAPI
from generate import initialized, ui
import pydantic
import gradio as gr


class Input(pydantic.BaseModel):
    prompts: list[str]
    temperature: float = 0.8
    top_p: float = 0.95

class Output(pydantic.BaseModel):
    results: list[str]

app = FastAPI()

@app.post("/prompt")
def prompt(_input: Input) -> Output:
    print("prompt", _input.prompts[0])
    results = initialized(
        _input.prompts[0],
        temperature=_input.temperature,
        top_p=_input.top_p,
    )
    return Output(results=[results])

app = gr.mount_gradio_app(app, ui, path="/webui")
