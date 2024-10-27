import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cuda:0"

tokenizer = AutoTokenizer.from_pretrained("glm-4-voice-9b", trust_remote_code=True)

tokenizer.chat_template = "{{role}}: {{content}}"

query = "你好"

inputs = tokenizer.apply_chat_template([{"role": "user", "content": query}],
add_generation_prompt=True,
tokenize=True,
return_tensors="pt",
return_dict=True
)

inputs = inputs.to(device)
model = AutoModelForCausalLM.from_pretrained(
"glm-4-voice-9b",
low_cpu_mem_usage=True,
trust_remote_code=True,
load_in_4bit=True
).eval()
model.save_pretrained("glm-4-voice-9b-int4")
tokenizer.save_pretrained("glm-4-voice-9b-int4")