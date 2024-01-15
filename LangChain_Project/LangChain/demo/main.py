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

def get_db_params():

    # 数据库连接参数
    db_params = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': 'aaqqRew???sett',
        'db': 'Stock_sh'
    }

    return db_params

def get_table_info(_):
    l = [10, 11 , 12]
    res = ""
    for x in l:
        res = res + support.generate_key_value_string(support.get_table_structure(get_db_params(),x))
        res += "\n"
    return res

# Database connection and LLM setup
llm = OpenAI(temperature=0, verbose=True)

q_origin = "2023年12月内,sh600570的走势怎么样?"
print(f"原始问题: {q_origin}")


# ================================================================================================
# 0.1. 问题分解
# ================================================================================================

def split_question():
    
    # Update the template based on the type of SQL Database like MySQL, Microsoft SQL Server and so on
    template = """
    Question: {question}

    根据问题,输出回答这个问题需要用到的数据指标
    举例子:
        要回答Trend类的问题,可以计算Days of consecutive increase, maximum gain, maximum drawdown
        要回答Overview累的问题,可以计算Average, volatility

    """


    # Step 1
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", 
                '用中文仅输出要用的数据指标'
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

    data_field = select_chain.invoke({"question": f"{q_origin}"})

    print("指标提取：")
    print(data_field)
    print("=================================================================================")
    print("=================================================================================")

    return data_field


# ================================================================================================
# 0.3. 问题整合
# ================================================================================================

def integral_question():
    
    # Update the template based on the type of SQL Database like MySQL, Microsoft SQL Server and so on
    template = """
    Question and possible data: {q}

    根据原问题和可能要用的指标,整合出一个新的更易执行的问题
    Output:
    """

    # Step 1
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", 
                '输出整合好的问题'
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

    res = select_chain.invoke({"q": f"{q}"})

    print("整合后的问题")
    print(res)
    print("=================================================================================")
    print("=================================================================================")

    return res






# ================================================================================================
# 1. 初步筛选
# ================================================================================================

def Selection1(_):
    # Update the template based on the type of SQL Database like MySQL, Microsoft SQL Server and so on
    template = """
    请根据附带的表结构信息，基于问题,
    筛选可能要用的表和字段

    table information:{schema}\n

    Question: {question}
    Output:
    """

    # Step 1
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", 
                '请从以下数据库表中找出与问题相关的表,字段及其对应数据类型,输出包含表,字段及其对应数据类型的key-value对,以json格式输出'
            ),
            ("human",template),
        ]
    )

    select_chain = (
        RunnablePassthrough.assign(schema=get_table_info)
        | prompt
        | llm.bind(stop=["\nSQLResult:"])
        | StrOutputParser()
    )

    res = select_chain.invoke({"question": f"{q}"})

    print("初次筛选结果: ")
    print(res)
    print("=================================================================================")
    print("=================================================================================")

    return res

# ================================================================================================
# 2.二次筛选
# ================================================================================================

def Selection2(_):
    template = """
    请根据附带的表结构信息,表的内容描述
    精确选择解决问题所需的表和字段

    Table Information: {schema}

    Table Description: {description}

    Question: {question}
    Output:
    """

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", 
                '请从以下表中确定解决问题需要的表,字段及其对应数据类型,输出包含表,字段及其对应数据类型的key-value对,以json格式输出'
            ),
            ("human",template),
        ]
    )


    sql_response = (
        RunnablePassthrough.assign(schema=Selection1,description=support.extract_table_info)
        | prompt
        | llm.bind(stop=["\nSQLResult:"])
        | StrOutputParser()
    )

    res = sql_response.invoke({"question": f"{q}"})
    print("二次筛选结果: ")
    print(res)
    print("=================================================================================")
    print("=================================================================================")

    return res

# ================================================================================================
# 3.生成sql语句
# ================================================================================================

def sql_query_generate_execute(_):
    template = """
    请根据相关表结构信息和和问题
    给出sql query

    Table Information: {schema}

    Question: {question}
    Output:
    """

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", 
                'No-preamble,仅输出sql query'
            ),
            ("human",template),
        ]
    )

    sql_response = (
        RunnablePassthrough.assign(schema=Selection2)
        | prompt
        | llm.bind(stop=["\nSQLResult:"])
        | StrOutputParser()
    )

    sql_query = sql_response.invoke({"question": f"{q}"})

    print("sql query生成结果: ")
    print(sql_query)
    print("=================================================================================")
    print("=================================================================================")


    res = support.execute_sql_query(get_db_params(),sql_query)
    print(f"\nthis is result: {res}\n")
    return sql_query,res


def answer():
    template = """
    请根据附带的用户问题,针对这个问题的sql query及sql query运行结果
    给出问题的回答

    sql query and execution result: {sql_All}

    Question: {question}
    Output:
    """

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", 
                'give human-like answers'
            ),
            ("human",template),
        ]
    )

    answers_response = (
        RunnablePassthrough.assign(sql_All=sql_query_generate_execute)
        | prompt
        | llm.bind(stop=["\nSQLResult:"])
        | StrOutputParser()
    )

    answer = answers_response.invoke({"question": f"{q}"})

    print(answer)

    return 

data_field = split_question()

q = q_origin + data_field
print(f"原问题 和 分析:{q}")
q = integral_question()
answer()

# print(get_table_info(None))
# sql_query_generate_execute(None)
# print(support.execute_sql_query(get_db_params(), "SELECT high FROM a_share_view WHERE stock_id = 'sh600570' AND date BETWEEN '2023-01-01' AND '2023-12-31' ORDER BY high DESC LIMIT 1;"))
   
