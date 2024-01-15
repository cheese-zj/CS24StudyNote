import re
import pymysql
import ast
import json
import cryptography
import datetime

def list_to_json_string(structure_list):
    try:
        # 将结构信息列表转换为JSON格式的字符串
        json_string = json.dumps(structure_list)
        return json_string
    except Exception as e:
        print("Error:", e)
        return None

def default(obj):
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()

def get_table_structure(db_params, table_index):
    # 建立数据库连接
    connection = pymysql.connect(host=db_params['host'],
                                 user=db_params['user'],
                                 password=db_params['password'],
                                 db=db_params['db'],
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # 获取所有表的列表
            cursor.execute("SHOW TABLES")
            result = cursor.fetchall()

            # 检查结果并提取表名
            if result:
                # 假设第一个键包含表名
                first_key = next(iter(result[0]))
                tables = [item[first_key] for item in result]

                # 检查序号是否在范围内
                if table_index >= len(tables):
                    return json.dumps({"error": "Table index out of range."}, default=default)

                # 获取特定表的结构
                table_name = tables[table_index]
                cursor.execute(f"DESCRIBE {table_name}")
                table_structure = cursor.fetchall()

                # 获取表中前两行示例数据
                cursor.execute(f"SELECT * FROM {table_name} LIMIT 2")
                sample_data = cursor.fetchall()

                # 将结果封装为JSON
                table_info = {
                    'structure': table_structure,
                    'sample_data': sample_data
                }

                result_json = json.dumps({
                    'table_name': table_name, 
                    'table_info': table_info
                }, default=default)

                return result_json
            else:
                return json.dumps({"error": "No tables found."}, default=default)

    finally:
        connection.close()


def execute_sql_query(db_params, query):
    """
    执行 SQL 查询并返回结果。
    
    参数:
        db_params: 包含数据库连接信息的字典，例如主机名、用户名、密码等。
        query: 要执行的 SQL 查询字符串。
        
    返回:
        查询结果，通常是一个字典列表。
    """
    # 建立数据库连接
    connection = pymysql.connect(host=db_params['host'],
                                 user=db_params['user'],
                                 password=db_params['password'],
                                 db=db_params['db'],
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # 执行 SQL 查询
            cursor.execute(query)

            # 获取查询结果
            result = cursor.fetchall()
            return result

    except Exception as e:
        # 返回错误信息
        return {"error": str(e)}

    finally:
        # 关闭数据库连接
        connection.close()

def generate_key_value_string(data):
    # 首先检查data是否为字符串，如果是，则尝试将其解析为字典
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except json.JSONDecodeError:
            # 如果data不是有效的JSON字符串，则返回错误消息
            return "Invalid data: Not a valid JSON string."

    # 然后进行正常的处理
    key_value_pairs = []
    for key, value in data.items():
        key_value_pairs.append(f"{key}: {value}")
    result_string = ", ".join(key_value_pairs)
    return result_string

def extract_table_info(_):
    json_file_path = 'config.json'
    result = {"tables/views": []}  # 创建一个包含表格信息的字典
    
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if 'tables/views' in data:
                table_info = data['tables/views']
                for info in table_info:
                    table_name = info.get('table_name', '')
                    description = info.get('description', '')
                    table_data = {"table_name": table_name, "description": description}
                    result["tables/views"].append(table_data)  # 将每个表格信息添加到结果字典中
            else:
                print("JSON文件格式不正确，缺少 'tables/views' 键。")
    except FileNotFoundError:
        print(f"找不到文件：{json_file_path}")
    except json.JSONDecodeError:
        print(f"无法解析JSON文件：{json_file_path}")
    
    return result  # 返回包含表格信息的字典

