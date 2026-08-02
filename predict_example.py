import os
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.preprocessing import normalize

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

cfg = json.load(open(os.path.join(BASE_DIR, "config.json")))

OPTIONS = cfg["options"]

model = SentenceTransformer(cfg["primary_encoder"])


def predict(question, options):
    q = normalize(model.encode([question], convert_to_numpy=True))[0]
    o = normalize(model.encode(list(options), convert_to_numpy=True))
    scores = o @ q
    order = np.argsort(-scores)

    return [OPTIONS[i] for i in order[:3]], scores