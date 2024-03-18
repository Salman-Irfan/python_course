import time


def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.4f} seconds")
        return result

    return wrapper


# Applying the decorator to functions
@log_execution_time
def process_data(data):
    # Simulating data processing
    time.sleep(2)
    print("Data processed successfully")


@log_execution_time
def generate_report(report_name):
    # Simulating report generation
    time.sleep(1)
    print(f"Report '{report_name}' generated")


# Usage example
process_data([1, 2, 3])
generate_report("Sales Report")
