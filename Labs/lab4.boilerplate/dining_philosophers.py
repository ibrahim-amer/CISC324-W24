import threading
import time
import random

# Define the number of philosophers / forks
PHILOSOPHERS_COUNT = 5
thinking_time = 1
eating_time = 5
# Initialize locks for each fork
# TODO: create a list of forks using a semaphore for each fork
forks = []
mutex = threading.Semaphore(1)


def philosopher(id):

    while True:
        # Think
        print(f"Philosopher {id} is thinking.")
        # Simulate thinking time
        time.sleep(random.randint(1, thinking_time))

        # TODO: You should protect the critical section before executing the code below

        left_fork = id
        right_fork = (id + 1) % PHILOSOPHERS_COUNT
        # Pick up forks
        print(f"Philosopher {id} is hungry.")
        # TODO: pick up the left fork

        print(f"Philosopher {id} picked up left fork.")
        # TODO: pick up the right fork

        print(f"Philosopher {id} picked up right fork.")

        # TODO: You should release the lock for the critical section after executing the code above

        # Eat
        # Simulate eating time
        print(f"Philosopher {id} is eating.")
        time.sleep(random.randint(1, eating_time))

        # Put down forks
        # TODO: put down the left fork

        # TODO: put down the right fork

        print(f"Philosopher {id} finished eating and put down forks.")


if __name__ == "__main__":
    # Create and start philosopher threads
    philosophers = [threading.Thread(
        target=philosopher, args=(i,)) for i in range(PHILOSOPHERS_COUNT)]
    for p in philosophers:
        p.start()

    # Wait for all threads to finish
    for p in philosophers:
        p.join()
