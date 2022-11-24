import os
import yaml

params = yaml.safe_load(open('infra\env-vars.json'))


for i in params.keys():
    print(f"adding key: {i} to env")
    os.environ[i] = params[i]

 