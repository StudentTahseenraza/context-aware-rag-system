import faiss
import numpy as np

dimension = 384
index = faiss.IndexFlatL2(dimension)

memory_vectors = []

def add_vector(vector):
    vec = np.array([vector]).astype('float32')
    index.add(vec)
    memory_vectors.append(vector)

def search_vector(vector, k=1):
    vec = np.array([vector]).astype('float32')
    distances, indices = index.search(vec, k)
    return indices