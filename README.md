# Local-LLM-Chatbot

# Resources

</br>To set up our Python environment, I need to install the necessary packages and download the LLM model from Hugging Face.
### [Hugging Face](https://huggingface.co/)

* The Orca Model's Model Card: https://huggingface.co/zoltanctoth/orca_mini_3B-GGUF
</br>I used the 'Orca Mini 3B' model because it is small enough to run on Codespaces while still being complex enough to provide meaningful answers to the questions.



# Steps

* In the Terminal type this command to install the "ctransformers" Library:

<pre>
pip install ctransformers
</pre>

* create a new file name "Chat.py" to download our Model there.
</br>paste the model repository and model name into our code

* import the class that help us to download & use a large language model.
<pre>
from ctransformers import AutoModelForCausalLM
</pre>

* Create an object from the LLM model and give the necessary informations to it (The branch Id and the model name)
<pre>
llm = AutoModelForCausalLM.from_pretrained(
    "zoltanctoth/orca_mini_3B-GGUF", model_file="orca-mini-3b.q4_0.gguf"
)
</pre>

* If I write a simple program like the 1 which is written in "Chat1.py" file all the answers apear suddenly on the screen while I want it apears word by word like the one in ChatGPT so I modified it as "Chat2.py"

* I updated more code to have a simple chat prompt in "Chat3.py"

* I Updated the LLM logic to use the chat-optimized version of Meta's Llama2, which is much larger model than Orca, so it might be significantly slower! I added the code in "Chat4.py"

* I now want to implement conversational memory because, so far, my model only reacts to individual prompts without retaining context. To achieve this, I need to inject the conversation history into the prompt, ensuring that the model can maintain memory and respond accordingly. "Chat5.py"

### building a UI for my chatbot

* Now I want to build a UI for my chatbot using [Chainlit](https://docs.chainlit.io/get-started/overview), which is an excellent tool for building local LLM-based chatbots. Alternatively, I could use Streamlit, which is one of the most popular Python packages for creating interactive UIs. However, Streamlit primarily focuses on integrating with OpenAI and ChatGPT rather than supporting local LLMs. 

for using Chainlit I need to install it: 
<pre>
pip install chainlit
</pre>

Next, I need to implement the 'Message' feature from the 'Basic Concepts' section on the left sidebar.


