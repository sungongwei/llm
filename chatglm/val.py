
from transformers import AutoTokenizer, AutoModel
import typer
from typing import Annotated, Union
import json
from pathlib import Path

app = typer.Typer(pretty_exceptions_show_locals=False)


@app.command()
def main(
        model_dir: Annotated[str, typer.Argument(help='')],
        out_dir: Annotated[str, typer.Option(help='')],
):
  tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
  model = AutoModel.from_pretrained(model_dir, trust_remote_code=True, device='cuda')
  model = model.eval()
  output =[]
  right=0
  error=0
  all=0
  with open('a.json', 'r', encoding="utf-8") as f:
    list = json.load(f)
    for item in list:
      for q in item['list']:
        response, history = model.chat(tokenizer, q, history=[])
        print('user: ', q)
        print('assistant: ', response)
        all+=1
        if response != item['answer']:
          output.append({'question': q, 'response': response, 'answer': item['answer']})
          error+=1
        else:
          right+=1
    print(f'right: {right}, error: {error}, all: {all}')
    outf = open('val_out.json', 'w',encoding='utf-8')
    outf.write(json.dumps(output,ensure_ascii=False))
    outf.close()


if __name__ == '__main__':
    app()
