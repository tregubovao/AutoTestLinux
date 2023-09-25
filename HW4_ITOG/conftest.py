import pytest
from sshcheckers import ssh_checkout
import random, string
import yaml
from datetime import datetime

with open('config.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def make_folders():
    return ssh_checkout(data["IP_address"], data["user"], data["passwd"],
                        f'mkdir {data["folder_in"]} {data["folder_out"]} {data["folder_ext"]} {data["folder_ext2"]}',
                        "")


@pytest.fixture()
def make_files():
    return ssh_checkout(data["IP_address"], data["user"], data["passwd"],
                        f"cd {data['folder_in']}; touch file1 file2",
                        "")


@pytest.fixture()
def bad_arch():
    ssh_checkout(data["IP_address"], data["user"], data["passwd"],
                 f'cd {data["folder_in"]}; 7z a {data["folder_out"]}/arxbad -t{data["type"]}',
                 "Everything is Ok")
    ssh_checkout(data["IP_address"], data["user"], data["passwd"],
                 f'truncate -s 1 {data["folder_out"]}/arxbad.{data["type"]}',
                 "Everything is Ok")
    yield "arxbad"
    ssh_checkout(data["IP_address"], data["user"], data["passwd"],
                 f'rm -f {data["folder_out"]}/arxbad.{data["type"]}', "")


@pytest.fixture(autouse=True)
def print_time():
    print("Start: {}".format(datetime.now().strftime("%H:%M:%S.%f")))
    yield print("Stop: {}".format(datetime.now().strftime("%H:%M:%S.%f")))
