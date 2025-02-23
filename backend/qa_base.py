from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

qa_base = [
    # 🔹 CAMBIO CLIMÁTICO
    {"question": "Que es el cambio climatico?", "answer": "El cambio climatico es la variacion a largo plazo de los patrones del clima en la Tierra debido a factores naturales y actividades humanas."},
    {"question": "Cuales son las principales causas del cambio climatico?", "answer": "Las principales causas incluyen la quema de combustibles fosiles, la deforestacion y la produccion industrial que generan gases de efecto invernadero."},
    {"question": "Como afecta el cambio climatico al planeta?", "answer": "Provoca aumento de temperaturas, cambios en patrones de lluvia, deshielo de los polos y eventos climaticos extremos."},
    {"question": "Que es el efecto invernadero?", "answer": "Es el fenomeno por el cual ciertos gases retienen el calor en la atmosfera, manteniendo la temperatura de la Tierra."},
    {"question": "Cuales son los gases de efecto invernadero?", "answer": "Incluyen el dioxido de carbono (CO2), metano (CH4), oxidos de nitrogeno (NOx) y vapor de agua."},

    # 🔹 ENERGÍAS RENOVABLES
    {"question": "Que son las energias renovables?", "answer": "Son fuentes de energia que se regeneran naturalmente, como la solar, eolica, hidroelectrica y geotermica."},
    {"question": "Cuales son las ventajas de la energia solar?", "answer": "Es inagotable, no contamina y puede instalarse en zonas remotas sin acceso a la red electrica."},
    {"question": "Como funciona la energia eolica?", "answer": "Los aerogeneradores convierten la energia cinetica del viento en electricidad mediante turbinas."},
    {"question": "Que impacto tiene la energia hidroelectrica?", "answer": "Es una fuente renovable pero puede afectar los ecosistemas acuaticos y desplazar comunidades."},
    {"question": "Es la biomasa una energia limpia?", "answer": "Si bien proviene de residuos organicos, su combustion puede generar emisiones si no se controla adecuadamente."},

    # 🔹 SOSTENIBILIDAD
    {"question": "Que es la sostenibilidad?", "answer": "Es la capacidad de satisfacer las necesidades actuales sin comprometer los recursos de las futuras generaciones."},
    {"question": "Como podemos reducir nuestra huella de carbono?", "answer": "Optimizando el consumo de energia, usando transporte publico, reduciendo residuos y consumiendo productos locales."},
    {"question": "Que es la economia circular?", "answer": "Es un modelo que busca reducir el desperdicio, reutilizando y reciclando productos para minimizar el impacto ambiental."},
    {"question": "Cuales son las tres R de la sostenibilidad?", "answer": "Reducir, Reutilizar y Reciclar, principios clave para minimizar el impacto ambiental."},
    {"question": "Como afecta la deforestacion al medio ambiente?", "answer": "Reduce la biodiversidad, aumenta las emisiones de CO2 y altera los ciclos hidrologicos."},

    # 🔹 INNOVACIÓN TECNOLÓGICA
    {"question": "Que es una red inteligente de energia?", "answer": "Es un sistema electrico avanzado que optimiza el consumo y distribucion de energia usando tecnologia digital."},
    {"question": "Como se usa la inteligencia artificial en energias renovables?", "answer": "La inteligencia artificial puede ser usada para predecir patrones climaticos, optimizar la generacion de energia y mejorar la eficiencia de los sistemas."},
    {"question": "Que tecnologias permiten almacenar energia renovable?", "answer": "Las baterias de iones de litio, el almacenamiento hidraulico y las celdas de hidrogeno."},
    {"question": "Que impacto tiene la nanotecnologia en la energia solar?", "answer": "Permite fabricar paneles solares mas eficientes y ligeros, mejorando la conversion de energia."},
    {"question": "Que son los edificios autosuficientes?", "answer": "Son construcciones que generan su propia energia y minimizan su impacto ambiental."}
]


# Cargamos el modelo de embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

# Convertimos todas las preguntas en vectores
questions = [item["question"] for item in qa_base]
question_embeddings = model.encode(questions)

# Creamos un índice FAISS para búsquedas eficientes
dimension = question_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(question_embeddings))

# Guardamos los embeddings en un archivo para no recalcular cada vez
faiss.write_index(index, "qa_index.faiss")
np.save("qa_questions.npy", questions)