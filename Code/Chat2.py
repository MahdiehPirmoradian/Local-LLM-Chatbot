from ctransformers import AutoModelForCausalLM

llm = AutoModelForCausalLM.from_pretrained("zoltanctoth/orca_mini_3B-GGUF", model_file="orca-mini-3b.q4_0.gguf")

prompt = "The capital city of Iran is"

#I add "flush=True" to put the words on the screen as soon as it apears
for tocken in llm(prompt, stream=True):
    print(tocken, end='', flush=True)

