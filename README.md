# MedicalChatbotUsingLlama2

![](E:\Self\MedicalChatbotUsingLlama2\static\images\medical-chatbot-demo-screenshot-1.png)
![](E:\Self\MedicalChatbotUsingLlama2\static\images\medical-chatbot-demo-screenshot.png)

# How to run?

### STEPS:

Clone the repository

```bash
git clone https://github.com/princejaiswal03/MedicalChatbotUsingLlama2.git
```

### STEP 01- Create a virtual environment after opening the repository with python 3.9

```bash
python3 -m venv <myenvpath>
```

```bash
source <myenvpath>/bin/activate
or 
source <myenvpath>/Scripts/activate

```

### STEP 02- install the requirements

```bash
pip install -r requirements.txt
```

### Create a `.env` file in the root directory and add your Pinecone credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PINECONE_API_ENV = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### Download the quantize model from the link provided in model folder & keep the model in the model directory:

```ini
## Download the Llama 2 Model and keep in model directory inside project root directory:

llama-2-7b-chat.ggmlv3.q4_0.bin


## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```

```bash
# run the following command to store vectors into Pinecone Index
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,

```bash
open up localhost: http://localhost:8080
```

#### To use ngrok, auth token is required. Use below command to authenticate ngrok

```bash
ngrok config add-authtoken <ngrok-auth-token>

```

### Techstacks Used:

- Python
- LangChain
- Flask
- Meta Llama2
- Pinecone