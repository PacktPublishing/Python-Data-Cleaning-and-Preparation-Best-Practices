from queue import Queue

def read_message_queue():
    q = Queue()
    
    # Adding messages to the queue
    for i in range(10):  # Mocking messages
        q.put(f"message {i}")
    
    # Reading and processing messages from the queue
    while not q.empty():
        message = q.get()
        process_message(message)
        q.task_done()  # Signal that the task is done

def process_message(message):
    print(f"Processing message: {message}")

# Example usage
read_message_queue()
