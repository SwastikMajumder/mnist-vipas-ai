import numpy as np
import base64

def pre_process(input):
    return np.frombuffer(base64.b64decode(input), dtype=np.float32).tolist()
def post_process(input):
    return base64.b64encode(np.array(input, dtype=np.float32).tobytes()).decode('utf-8')
