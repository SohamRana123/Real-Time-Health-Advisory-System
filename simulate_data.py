
# Simulate Real-Time Data Streaming
import time
import random

def generate_data():
    while True:
        yield {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "heart_rate": random.randint(60, 120),
            "steps": random.randint(1000, 10000),
            "calories": random.randint(50, 500),
        }

# Save simulated data to a file
def save_to_file():
    with open("data_stream.txt", "a") as f:
        for data in generate_data():
            f.write(f"{data}\n")
            time.sleep(1)  # Simulate a 1-second delay

if __name__ == "__main__":
    save_to_file()
