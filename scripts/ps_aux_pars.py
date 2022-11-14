from datetime import datetime
from subprocess import (
    run, PIPE
)


def user_list():
    data = run(["ps", "-e", "-o", "user"], stderr=PIPE, stdout=PIPE)
    users = []
    raw = data.stdout.decode("utf-8").replace(" ", "").split("\n")[1:]
    [users.append(x) for x in raw if x not in users]
    return users


def number_active_processes(username: str = None):
    if username:
        res = run([f"ps -U {username} | wc -l"], shell=True, stderr=PIPE, stdout=PIPE)
    else:
        res = run(["ps -e | wc -l"], shell=True, stderr=PIPE, stdout=PIPE)
    return res.stdout.decode("utf-8").replace(" ", "")[:-1]


def biggest_cpu_consumer():
    data = run(["ps aux -r | head -2"], shell=True, stderr=PIPE, stdout=PIPE)
    raw = data.stdout.decode("utf-8").split(" ").pop()
    if len(raw) > 20:
        return raw[:20]
    return raw


def biggest_memory_consumer():
    data = run(["ps aux -m | head -2"], shell=True, stderr=PIPE, stdout=PIPE)
    raw = data.stdout.decode("utf-8").split(" ").pop()
    if len(raw) > 20:
        return raw[:20]
    return raw


def total_memory_usage():
    data = run(["ps -e -o %mem | awk '{s+=$1} END {print s}'"], shell=True, stderr=PIPE,
               stdout=PIPE)
    return data.stdout.decode("utf-8").replace("\n", "")


def total_cpu_usage():
    data = run(["ps -e -o %cpu | awk '{s+=$1} END {print s}'"], shell=True, stderr=PIPE,
               stdout=PIPE)
    return data.stdout.decode("utf-8").replace("\n", "")


def collect_result():
    date = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
    users = user_list()
    with open(f'./src/{date}_system_states.txt', "w+") as f:
        f.write(f"Users: {users}\n")
        f.write(f"Total number of processes: {number_active_processes()}\n")
        f.write("User's processes:\n")
        for user in users:
            f.write(f"{user}: {number_active_processes(user)}\n")
        f.write(f"Total memory usage: {total_memory_usage()}\n")
        f.write(f"Total CPU usage: {total_cpu_usage()}\n")
        f.write(f"Biggest memory consumer: %{biggest_memory_consumer()}\n")
        f.write(f"Biggest CPU consumer: %{biggest_cpu_consumer()}\n")


if __name__ == '__main__':
    collect_result()
