import threading
import requests
import multiprocessing

val = 0

mutex = threading.Lock()


def print_thread(to_print):

    print(to_print)

def ask_request():
    global val
    try:
        mutex.acquire()
        val += 1
        mutex.release()
        req = requests.get("http://www.mnit.ac.in/")
        req = requests.get("http://tmc.ac.in/")
        req = requests.get("http://www.tripurachemicalsoc.com/")
        printer = threading.Thread(target=print_thread, args=("Status code received " + str(req.status_code) + " request number " + str(val), ))
        printer.start()
    except:
        print("SOMething did go wrong here", multiprocessing.cpu_count())

def thread():
    global val
    try:
        request = threading.Thread(target=ask_request, args=())
        request.start()

        printer = threading.Thread(target=print_thread, args=("Attempting to requesst the page", ))
        printer.start()
        
    except:
        printer = threading.Thread(target=print_thread, args=("This request did'nt go through", ))
        printer.start()
        
    thread1 = threading.Thread(target=thread, args=())
    thread2 = threading.Thread(target=thread, args=())

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()



if __name__ == "__main__":

    # 19 sec to 1000
    
    thread1 = threading.Thread(target=thread, args=())
    thread1.start()
    thread1.join()
    print("WOrk done from main progrma")