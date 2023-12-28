from langchain.llms import OpenAI
llm = OpenAI()
question = "你是哪个模型呀"
print("你是哪个模型呀")
print(llm.predict(question))