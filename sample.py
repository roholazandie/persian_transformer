from transformers import GPT2Tokenizer

cached_dir = "/home/rohola/codes/persian_transformer/tokenizer_cache"
tokenizer = GPT2Tokenizer.from_pretrained('gpt2', cache_dir=cached_dir)
tokens = tokenizer.tokenize("this is bullshit")
print(tokens)