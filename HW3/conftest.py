from task21 import find_text, get_stdout
import pytest
import yaml
from datetime import datetime

with open('config.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def make_folders():
    return find_text(f"mkdir -p {data['PATH_IN']} {data['PATH_OUT']} {data['PATH_EXT']}", '')


@pytest.fixture()
def make_files():
    return find_text(f"cd {data['PATH_IN']}; touch file1 file2", '')


@pytest.fixture(autouse=True)
def stat():
    yield
    stat = get_stdout("cat /proc/loadavg")
    find_text(f"echo 'time: {datetime.now()} count:{data['count']} size: {data['size']} load_stat: {stat}'>> stat.txt", "")
