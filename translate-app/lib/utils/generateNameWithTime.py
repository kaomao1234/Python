import datetime

def generate_name_with_time(base_name):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    generated_name = f"{base_name}_{current_time}"
    return generated_name


