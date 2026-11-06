# ЗАДАНИЕ 1: Распаковка списка и слияние

statuses = ["queued", "running", "testing", "deploy", "done"]

first, *middle, last = statuses
my_new_list = [*middle, "failed", "skipped"]

print("Задание 1")
print(f"first: {first}, last: {last},\nmy_new_list: {my_new_list}\n")

# ЗАДАНИЕ 2: Словарь, слияние и вызов функции

browser = {"browser": "chrome", "timeout": 3000}
options = {"headless": True, "timeout": 5000}


def start_session(browser, timeout, headless):
    return f"{browser}, timeout={timeout}, headless={headless}"


config = {**browser, **options}
result = start_session(**config)

print("Задание 2")
print(f"config: {config}\nresult: {result}")
