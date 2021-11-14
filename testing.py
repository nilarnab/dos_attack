import threading


def thread():
    print(val)
    print("the thread is being run")


if __name__ == "__main__":

    val = 10
    thread = threading.Thread(target=thread, args=())
    thread.start()

    thread.join()

