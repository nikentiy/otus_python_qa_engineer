from datetime import datetime
from functools import reduce
from subprocess import (
    PIPE, Popen
)


def collect_data() -> list:
    output = Popen(['ps', 'aux'], stdout=PIPE).stdout.readlines()
    headers = output[0].decode("utf-8").strip().split()
    raw_data = map(lambda s: s.decode("utf-8").strip().split(None, len(headers) - 1), output[1:])
    return [dict(zip(headers, process)) for process in raw_data]


def user_list(raw_data: list) -> list:
    users = []
    [users.append(x.get("USER")) for x in raw_data if x.get("USER") not in users]
    return users


def number_active_processes(username: str, raw_data: list) -> int:
    counter = 0
    for proc in raw_data:
        if proc.get("USER") == username:
            counter += 1
    return counter


def biggest_cpu_consumer(raw_data: list) -> str:
    proc = reduce(lambda x, y: y if float(x.get("%CPU")) < float(y.get("%CPU")) else x, raw_data)
    return proc.get("COMMAND")[:20]


def biggest_memory_consumer(raw_data: list) -> str:
    proc = reduce(lambda x, y: y if float(x.get("%MEM")) < float(y.get("%MEM")) else x, raw_data)
    return proc.get("COMMAND")[:20]


def total_memory_usage(raw_data: list) -> float:
    total_memory = 0
    for proc in raw_data:
        total_memory = total_memory + float(proc.get("%MEM"))
    return round(total_memory, 2)


def total_cpu_usage(raw_data: list) -> float:
    total_cpu = 0
    for proc in raw_data:
        total_cpu = total_cpu + float(proc.get("%CPU"))
    return round(total_cpu, 2)


def collect_result():
    date = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
    raw_data = collect_data()
    users = user_list(raw_data)
    result = f"Users: {users}\n" \
             f"Total number of processes: {len(raw_data)}\n" \
             f"Total memory usage: {total_memory_usage(raw_data)}\n" \
             f"Total CPU usage: {total_cpu_usage(raw_data)}\n" \
             f"The biggest memory consumer: %{biggest_memory_consumer(raw_data)}\n" \
             f"The biggest CPU consumer: %{biggest_cpu_consumer(raw_data)}\n" \
             f"User's processes:\n"
    for user in users:
        user_proc = f"{user}: {number_active_processes(user, raw_data)}\n"
        result = result + user_proc
    with open(f'./src/{date}_system_states.txt', "w+") as f:
        f.write(result)
        print(result)


if __name__ == '__main__':
    collect_result()
