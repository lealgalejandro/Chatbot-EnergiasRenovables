import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from qa_base import qa_base

# Cargamos el modelo y los datos
model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index("qa_index.faiss")
questions = np.load("qa_questions.npy", allow_pickle=True)

def get_response(user_input):
    # Convertimos la entrada del usuario en embedding
    user_embedding = model.encode([user_input])
    
    # Buscamos la pregunta más similar
    _, index_match = index.search(np.array(user_embedding), 1)
    
    # Obtenemos la pregunta más parecida
    matched_question = questions[index_match[0][0]]
    
    # Buscamos la respuesta correspondiente en qa_base
    for item in qa_base:
        if item["question"] == matched_question:
            return item["answer"]
    
    return "No tengo una respuesta para eso, pero puedo aprender si me lo explicas."
