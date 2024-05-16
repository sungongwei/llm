
python3 -m fastchat.serve.controller  > fastchat.log 2>&1 &

python3 -m fastchat.serve.model_worker --model-path ./chatglm3-6b-01/  > fastchat.log 2>&1 &

python -m fastchat.serve.openai_api_server --host localhost --port 8000 > fastchat.log 2>&1 &