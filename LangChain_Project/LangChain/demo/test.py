from langchain.chains import create_sql_query_chain
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
import support
import pymysql
import json
import cryptography

llm = OpenAI(temperature=0, verbose=True)

mail = '''

Dear professor

Hello，teacher. My name is Qian Yu.I am the citizen of China. I studied Chinese for many years.

I am interested in Chinese translation 1.

Could you please help me enroll it?

Thankyou very much！！！！My student id is 34038663

'''


# Update the template based on the type of SQL Database like MySQL, Microsoft SQL Server and so on
template = """
Original mail: {mail}
优化这封邮件,让它更加正式且流畅,称谓更合理
"""


# Step 1
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", 
            '用英文仅输出整篇邮件'
        ),
        ("human",template),
    ]
)

select_chain = (
    RunnablePassthrough.assign()
    | prompt
    | llm.bind(stop=["\nSQLResult:"])
    | StrOutputParser()
)

data_field = select_chain.invoke({"mail": f"{mail}"})


print(data_field)