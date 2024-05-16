import torch
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json
import time
# 打开 JSON 文件并读取数据
with open('a.json') as f:
    questions = json.load(f)

# 初始化Bert模型和tokenizer
start = time.time()
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
device = torch.device("mps")
tokenizer = BertTokenizer.from_pretrained("shibing624/text2vec-base-chinese")
model = BertModel.from_pretrained("shibing624/text2vec-base-chinese").to(device)
model.eval()
end = time.time()
print("加载模型:", end - start, "seconds")

# 1. 准备数据
# 2. 对问题进行编码和向量化
start = time.time()
question_vectors = []
for question in questions:
    inputs = tokenizer(question['title'], return_tensors="pt",max_length=512, padding=True, truncation=True).to(device)
    with torch.no_grad():
        outputs = model(**inputs)
        question_vector = torch.mean(outputs.last_hidden_state, dim=1).cpu().numpy()
        # question_vector = torch.mean(outputs.last_hidden_state, dim=1)
        question_vectors.append(question_vector)
end = time.time()
question_vectors_base = np.vstack(question_vectors)
# question_vectors_base = torch.vstack(question_vectors)
print("向量化:", end - start, "seconds")




def answer_question(user_input):
  start = time.time()
  user_inputs = tokenizer(user_input, return_tensors="pt",max_length=512, padding=True, truncation=True).to(device)
  with torch.no_grad():
      user_outputs = model(**user_inputs)
      user_vector = torch.mean(user_outputs.last_hidden_state, dim=1).cpu().numpy()
      # user_vector = torch.mean(user_outputs.last_hidden_state, dim=1)

  # 4. 计算相似度
  end = time.time()
  print("用户输入向量化:", end - start, "seconds")

  start = time.time()
  similarities = cosine_similarity(user_vector, question_vectors_base)[0]
  # similarities = torch.nn.functional.cosine_similarity(user_vector, question_vectors_base, dim=1).cpu().numpy()
  # print(similarities)
  end = time.time()
  print("计算相似度:", end - start, "seconds")

  # 对相似度进行排序
  # 获取相似度大于90%且最高的前三个结果
  threshold = 0.8
  sorted_indices = np.argsort(similarities)[::-1]
  matching_indices = [idx for idx in sorted_indices if similarities[idx] > threshold][:3]

  # 返回结果
  matching_results = [(questions[i]['title'], questions[i]['answer'], float(similarities[i])) for i in matching_indices]
  return matching_results