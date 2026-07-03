#获取对象
from urllib import response

from openai import OpenAI
client=OpenAI(
    api_key=("sk-0968146b2b9d4c829c93e9690eef4833"),
    base_url="https://ws-2mob3pcgzkkecd9h.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)
#调用模型
response=client.chat.completions.create(
    model="qwen3.7-max",
    messages=[
        {"role": "system","content": "你是一个python专家"},
        {"role": "assistant","content": "我是编程专家"},
        {"role": "user","content":"输出1-10的数字,使用python代码"}
    ]
)
#处理
print(response.choices[0].message.content)