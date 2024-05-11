import torch
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 初始化Bert模型和tokenizer
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
device = torch.device("mps" if torch.cuda.is_available() else "cpu")
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased").to(device)
model.eval()

# 1. 准备数据
questions = ["What is your name?", "How old are you?", "What do you do?"]
answers = ["My name is ChatGPT.", "I am 2 years old.", "I am an AI language model."]

# 2. 对问题进行编码和向量化
question_vectors = []
for question in questions:
    inputs = tokenizer(question, return_tensors="pt", padding=True, truncation=True).to(device)
    with torch.no_grad():
        outputs = model(**inputs)
        question_vector = torch.mean(outputs.last_hidden_state, dim=1).cpu().numpy()
        question_vectors.append(question_vector)

# 3. 用户查询
user_input = "how old are you"
user_inputs = tokenizer(user_input, return_tensors="pt", padding=True, truncation=True).to(device)
with torch.no_grad():
    user_outputs = model(**user_inputs)
    user_vector = torch.mean(user_outputs.last_hidden_state, dim=1).cpu().numpy()

# 4. 计算相似度
similarities = cosine_similarity(user_vector, np.vstack(question_vectors))
print(similarities)
# 5. 过滤结果
threshold = 0.9
matching_indices = np.where(similarities > threshold)[1]

# 6. 返回结果
matching_questions = [questions[i] for i in matching_indices]
matching_answers = [answers[i] for i in matching_indices]

print("Matching questions:", matching_questions)
print("Matching answers:", matching_answers)
