import threading
import requests
import multiprocessing
import time


mutex = threading.Lock()


def print_thread(to_print):

    print(to_print)

def ask_request(val):

    # req = requests.get("http://www.mnit.ac.in/")
    req = requests.get("http://www.tripurachemicalsoc.com/")
    printer = threading.Thread(target=print_thread, args=("Status code received " + str(req.status_code) + " request number " + str(val) + " >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", ))
    printer.start()

    # try:
       
        
    # except:
    #     print("SOMething did go wrong here", multiprocessing.cpu_count())

def thread(val):
    global currently_running

    currently_running += 1

    try:
        request = threading.Thread(target=ask_request, args=(val, ))
        request.start()
        
        request.join()

        printer = threading.Thread(target=print_thread, args=("Attempting to requesst the page", ))
        printer.start()

        printer.join()

        
        
    except:
        printer = threading.Thread(target=print_thread, args=("This request did'nt go through", ))
        printer.start()

    currently_running -= 1
        
    



if __name__ == "__main__":

    # MAX_ALLOWED = 2800
    MAX_ALLOWED = 5000
    # wait = 0.04
    wait = 0

    # 19 sec to 1000
    val = 0
    currently_running = 0
    # stable_value = 2100
    stable_value = 2500
    reached = False

    threads = []
    
    while True:
        if currently_running <= MAX_ALLOWED:
            val += 1
            print("Sending request thread number", val, "Currently running", currently_running, "waiting for", wait)

            time.sleep(wait)
            
            if not reached:
                wait = 0.001
    
            if currently_running < stable_value - 100:
                if reached:
                    wait = 0.005
            
            if currently_running > stable_value + 100:
                reached = True
                wait = 0.06

            thread1 = threading.Thread(target=thread, args=(val, ))
            thread1.start()
            threads.append(thread1)
        else:
            # print("NUmber oof threads running is", currently_running, "which eexceedes", MAX_ALLOWED)
            pass

    for thread in threads:
        thread.join()

    print("WOrk done from main progrma")