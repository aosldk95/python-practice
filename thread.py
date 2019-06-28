import threading
import queue

q=queue.Queue()
def on_thread_execute():
    while True:
        msg=q.get()
        print("from tread",msg) # 워커

t=threading.Thread(target=on_thread_execute)
t.start()

while True:
    msg=input()
    q.put(msg)
    print("from console:",msg) # 문제 제작자
    