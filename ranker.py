from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def score_sections(persona_job, sections):
    q_emb = model.encode([persona_job])
    sims = model.encode([s["text"] for s in sections])
    scores = cosine_similarity(q_emb, sims)[0]
    ranked = sorted(zip(scores, sections), key=lambda x: -x[0])
    return ranked

def extract_refined_text(section, max_tokens=200):
    text = section["text"]
    return text if len(text.split()) <= max_tokens else ' '.join(text.split()[:max_tokens])
