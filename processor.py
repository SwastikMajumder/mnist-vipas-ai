import numpy as np
import base64

def pre_process(input):
    return np.frombuffer(base64.b64decode(input), dtype=np.float32)
def post_process(input):
    return base64.b64encode(input.tobytes()).decode('utf-8')
