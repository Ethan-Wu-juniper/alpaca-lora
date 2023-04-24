from generate import initialized
import json
from tqdm.auto import tqdm
import time

with open("squad.jsonl", "r") as fp:
    data = [json.loads(line) for line in fp.readlines()]
    start_t = time.time()
    results = [initialized(d) for d in tqdm(data)]
    print(f"takes {time.time() - start_t} seconds")