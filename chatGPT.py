"""
    chatgpt 提问主要3种方式
    获取详细信息：
        请具体告诉我
        请提供具体案例
        情报的来源，出处，以及参考文章
        关于xxx详细说明
    寻求解决方案
        有比xxx更好的方法吗？
        如何才能做得更好？
        我现在能做得是什么？
    判断对错
        关于xxx，我的想法是这样的，这是对的吗
        做了xxx，会有用吗？
    表现要求
        请在xxx字以内
        以幽默风/鲁迅风/xxx风格
        尽量简短
        通俗易懂的回答
        条例式/口语化回答

API key: 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

"""
import openai
openai.api_key = "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"
# Set up the model ID
model_engine = "text-davinci-002"

# Ask a question and get the answer
prompt = "What is the meaning of life?"
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.7,
)
answer = response.choices[0].text.strip()

# Print the answer
print(answer)

