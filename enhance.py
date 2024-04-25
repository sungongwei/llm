import json
# from nlpcda import Simbert
# config = {
#         'model_path': '/xxxx/chinese_simbert_L-12_H-768_A-12',
#         'CUDA_VISIBLE_DEVICES': '0,1',
#         'max_len': 32,
#         'seed': 1
# }
# simbert = Simbert(config=config)

# with open('datasetdir/init/train.json', 'r', encoding="utf-8") as f:
#     for line in f:
#         data = json.loads(line)
#         synonyms = simbert.replace(sent=data['conversations'][0]['content'], create_num=20)
#         for item in synonyms:
#             print(item)
with open('a.json', 'r', encoding="utf-8") as f:
    list = json.load(f)
    for item in list:
      
      for q in item['list']:
        synonyms = simbert.replace(sent=q, create_num=20)
        for s in synonyms:
           print(s)
          # item['list'].append("111")

    f = open('out.json', 'w')
    f.write(json.dumps(list,ensure_ascii=False))
    f.close()
    