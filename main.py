import tokenizers
from tokenizers.processors import BertProcessing
from tokenizers import ByteLevelBPETokenizer

tokenizer = ByteLevelBPETokenizer(
    "models/faberto/vocab.json",
    "models/faberto/merges.txt",
)

tokenizer._tokenizer.post_processor = BertProcessing(
    ("</s>", tokenizer.token_to_id("</s>")),
    ("<s>", tokenizer.token_to_id("<s>")),
)
tokenizer.enable_truncation(max_length=512)

tokens = tokenizer.encode("این یک تست است.")
#print(tokenizer.encode("این یک تست است."))
#print(tokenizer.encode("this is a test"))