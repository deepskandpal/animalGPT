# animalGPT
LLM model which answers questions about [Animal (2023)](https://en.wikipedia.org/wiki/Animal_(2023_film))

## What is Available 
1. The platform is now [live](https://animalgpt-production.up.railway.app/) the instance needs to be deployed if the service is unavailable
2. The model is hosted on hugging face [link](https://huggingface.co/dkandpalz/animalGPT2)
3. Current Prediction pipeline is just text generation directly from the model for any user query


## What is coming next
1. text processing layer which will handle illegitimate and out of context queries
2. Embeddings model for model inference along with prompt Engineering for text generation to better understand user queries



## Additional tasks
1. Add user queries logging in the production app
2. Clean datasets from the better contextual understanding of the information (manual work)
3. Try out Q/A models like BERT and other GPT models like InstructGPT
4. Create Benchmarking for model performance comparison
