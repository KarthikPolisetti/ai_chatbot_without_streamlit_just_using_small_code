from dotenv import load_env
load_env()

from langchain_google_genai import ChatGoogleGenerativeAI
llm=ChatGoogleGenerativeAI(model="your model name") 

'''i used google gemini-3-flash-preview'''

while True:
  query=input("User:")
  if query.lower() in ["exit","bye","goodbye","quit"]:
    print("Exiting the chat,GoodBye")
    break
  res=llm.invoke(query)
  print("AI:",res.text,"/n")
  
