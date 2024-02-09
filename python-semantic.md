%pip install transformers
%pip install sentence-transformers
%pip install scikit-learn


from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
model = SentenceTransformer('all-MiniLM-L6-v2') 

sentence1 = "Benson and Hedges"
sentence2 = "Hedges AND Benson"
sentence3 = "Hedges AND Benson"
sentence4 = "HEDGES AND BENSON"
sentence5 = "hedges & benson"
sentence6 = "BENSON & HEDges"
sentence7 = "Jack And Jill"

# Encode sentences to get their embeddings  
embedding1 = model.encode(sentence1)
embedding2 = model.encode(sentence2)
embedding3 = model.encode(sentence3)
embedding4 = model.encode(sentence4)
embedding5 = model.encode(sentence5)
embedding6 = model.encode(sentence6)
embedding7 = model.encode(sentence7)
embeddings=[embedding1,embedding2,embedding3,embedding4,embedding5,embedding6,embedding7]

# Calculate cosine similarity between embeddings
sim = cosine_similarity(embeddings)
print(sim)
print("Similarity score:", sim[0][0])


import pandas as pd

df1 = pd.read_csv("source1.csv") 
df2 = pd.read_csv("source2.csv")

source1_name_field = df1['name'].tolist()
source2_customer_field = df2['customer'].tolist()


import numpy as np
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')

emb_source1_name_field = model.encode(source1_name_field) 
emb_source1_name_field = model.encode(source2_customer_field)

from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(emb_source1_name_field, emb_source1_name_field)

print(similarity)
indices = np.argmax(similarity, axis=1)


for i in range(len(indices)):
  print(source1_name_field[i], source2_customer_field[indices[i]])


  
