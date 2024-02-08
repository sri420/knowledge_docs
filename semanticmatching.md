Here is a Python code snippet to demonstrate how you could implement semantic matching with word embeddings for joining two data sources:

```python
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import gensim.models.keyedvectors as word2vec

# Load sample customer name data from two data sources   
df1 = pd.DataFrame({"id":[1,2,3], "name":["John Dow", "Sarah Connor", "MikeDavis"]}) 

df2 = pd.DataFrame({"id":[10,11], "name":["J Dow", "Mike Daves"]})

# Load pre-trained word2vec model 
model = word2vec.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)  

# Get word vectors for each name text
vectors1 = [model.get_vector(i) for i in df1.name]  
vectors2 = [model.get_vector(j) for j in df2.name]

# Calculate cosine similarity between all combinations
similarity = cosine_similarity(vectors1, vectors2)

# Check similarities above threshold 
matches = similarity > 0.70  

# Join data frames on matched vectors
df_joined = pd.merge(df1, df2, left_on=matches.idxmax(1), right_index=True)

print(df_joined)
```

This calculates cosine similarity between pre-trained word vectors and joins records above a threshold. Let me know if you have any other questions!
