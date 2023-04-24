from generate import initialized
import json

with open("squad.jsonl", "r") as fp:
    data = [json.loads(line) for line in fp.readlines()]
    results = [initialized(d) for d in data]