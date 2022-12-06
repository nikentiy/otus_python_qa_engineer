import argparse
import json
import re
from collections import Counter
from datetime import datetime
from subprocess import run, PIPE

LOG_TEMPLATE = "(?P<ip>.*?) .* \[(?P<date>.*?)(?= ) (?P<timezone>.*?)\] \"(?P<method>.*?) (?P<path>.*?)(?P<request_version> HTTP/.*)?\" (?P<status>.*?) (?P<length>.*?) \"(?P<referrer>.*?)\" \"(?P<user_agent>.*?)\" (?P<time>[0-9]+)"


def write_result(data: dict):
    date = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
    with open(f'./{date}_logs_parser_results.txt', "w+") as f:
        s = json.dumps(data, indent=4)
        f.write(s)


def get_files_in_dir(path: str):
    output = run([f'find {path} -type f -name \"*.log\"'], shell=True, stdout=PIPE, stderr=PIPE).stdout
    return output.decode("utf-8").strip().split()


def read_file(path: str) -> list:
    with open(path, newline='') as f:
        return f.readlines()


def collect_data(raw_data: list):
    ips = []
    methods = []
    times = []
    requests = []
    for line in raw_data:
        data = re.match(LOG_TEMPLATE, line)
        ips.append(data.group("ip"))
        methods.append(data.group("method"))
        times.append(int(data.group("time")))
        requests.append(data)
    return ips, methods, times, requests


def top_3_ips(ips: list):
    return sorted(Counter(ips))[-3:]


def count_methods(methods: list):
    return dict(Counter(methods))


def top_3_times(times: list):
    return sorted(times)[-3:]


def find_request_by_time(requests: list, times: list):
    res = []
    for request in [request for request in requests if int(request.group("time")) in times][:3]:
        res.append({
                    "date": request.group('date'),
                    "method": request.group('method'),
                    "ip": request.group('ip'),
                    "path": request.group('path'),
                    "time": request.group('time')
                })
    return res


def main(raw_data: list):
    ips, methods, times, requests = collect_data(raw_data)
    result = {
        "top 3 IPs": top_3_ips(ips),
        "count of methods": count_methods(methods),
        "top 3 the longest requests": find_request_by_time(requests, top_3_times(times))
    }
    write_result(result)
    print(result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Script to pars logs from a file or a directory",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-f", "--file", dest='file', type=str, default=None,
                        help="path to a log file to pars")
    parser.add_argument("-d", "--dir", dest='dir', type=str, default=None,
                        help="path to a directory with log files to pars")
    args = parser.parse_args()
    assert (args.file or args.dir), "you must specify either a directory or a file"
    raw_data = []
    if args.file:
        raw_data.extend(read_file(args.file))
    elif args.dir:
        for file in get_files_in_dir(args.dir):
            raw_data.extend(read_file(file))
    main(raw_data)
