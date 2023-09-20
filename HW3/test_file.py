# Дополнить проект фикстурой, которая после каждого шага теста
# дописывает в заранее созданный файл stat.txt строку вида:
# время, кол-во файлов из конфига, размер файла из конфига,
# статистика загрузки процессора из файла /proc/loadavg
# (можно писать просто всё содержимое этого файла).

from task21 import find_text
import pytest
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)


class TestPositive:
    def test_step1(self, make_folders, make_files):
        assert find_text(f"cd {data['PATH_IN']}; 7z a {data['PATH_OUT']}/arch1 -t{data['type_of_arch']}",
                         "Everything is Ok"), 'test_step1 FAIL'

    def test_step3(self):
        assert find_text(f"cd {data['PATH_NEW']}; 7z u {data['PATH_OUT']}/arch1.{data['type_of_arch']}",
                         "Everything is Ok"), 'test_step3 FAIL'

    def test_step4(self):
        res_list4 = [find_text(f"cd {data['PATH_OUT']}; 7z l arch1.{data['type_of_arch']}", "file1"),
                     find_text(f"cd {data['PATH_OUT']}; 7z l arch1.{data['type_of_arch']}", "file2"),
                     find_text(f"cd {data['PATH_OUT']}; 7z l arch1.{data['type_of_arch']}", "file5")
                     ]
        assert all(res_list4), 'test_step4 FAIL'


if __name__ == '__main__':
    pytest.main(['-vv'])
