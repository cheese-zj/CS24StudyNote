import queue
import threading
import time

# 创建一个队列
my_queue = queue.Queue()

# 生产者线程
def producer():
    for i in range(5):
        my_queue.put(i)  # 将数字放入队列
        print(f"Produced: {i}")
        print(f"Queue Status: {list(my_queue.queue)}")  # 打印队列状态


    my_queue.put(None)  # 放置退出标志

# 消费者线程
def consumer():
    while True:
        number = my_queue.get()
        if number is None:  # 如果获取到退出标志
            break  # 退出循环
        print(f"Consumed: {number}")
        print(f"Queue Status: {list(my_queue.queue)}")  # 打印队列状态
        my_queue.task_done()

# 创建生产者和消费者线程
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# 启动线程
producer_thread.start()
consumer_thread.start()

# 等待线程结束
producer_thread.join()
consumer_thread.join()

