from pathlib import Path

from tokenizers import ByteLevelBPETokenizer


clean_wiki_text = "/home/rohola/codes/persian_transformer/clean_wiki_text_txt"
paths = [str(x) for x in Path(clean_wiki_text).glob("**/*.txt")]

# Initialize a tokenizer
tokenizer = ByteLevelBPETokenizer()

# Customize training
tokenizer.train(files=paths, vocab_size=52000, min_frequency=2, special_tokens=[
    "<s>",
    "<pad>",
    "</s>",
    "<unk>",
    "<mask>",
])

# Save files to disk
tokenizer.save("models/faberto", "faberto")
