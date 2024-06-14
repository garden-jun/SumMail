import torch
from kobart import get_kobart_tokenizer
from transformers.models.bart import BartForConditionalGeneration

def load_model():
    model = BartForConditionalGeneration.from_pretrained('./kobart_summary')
    return model

def summarize_text(contents, length):
    model = load_model()
    tokenizer = get_kobart_tokenizer()
    
    contents = contents.replace('\n', '')
    input_ids = tokenizer.encode(contents)
    input_ids = torch.tensor(input_ids)
    input_ids = input_ids.unsqueeze(0)
    
    output = model.generate(input_ids, eos_token_id=1, max_length=length, num_beams=5)
    summary = tokenizer.decode(output[0], skip_special_tokens=True)
    
    return summary
