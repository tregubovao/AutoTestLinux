# Задание 1.
# Условие:
# Дополнить проект тестами, проверяющими команды вывода списка файлов (l)
# и разархивирования с путями (x).

from task21 import find_text
import pytest

PATH_IN = '/home/user/AT/in'
PATH_OUT = '/home/user/AT/out'
PATH_NEW = '/home/user/AT/new'
PATH_EXT = '/home/user/AT/ext'
PATH_EXT_X = '/home/user/AT/ext-x'


#
# def test_step1():
#     assert find_text(f'cd {PATH_IN}; 7z a {PATH_OUT}/arch1', "Everything is Ok"), 'test_step1 FAIL'
##
# def test_step3():
#     assert find_text(f'cd {PATH_NEW}; 7z u {PATH_OUT}/arch1', "Everything is Ok"), 'test_step3 FAIL'

# def test_step4():
#     assert find_text(f'cd {PATH_OUT}; 7z l arch1.7z', "Listing archive: arch1.7z"), 'test_step4 FAIL'

def test_step4():
    # проверка команды вывода списка файлов (l)
    res_list4 = [find_text('cd {}; 7z l arch1.7z'.format(PATH_OUT, PATH_EXT), "file1"),
                 find_text('cd {}; 7z l arch1.7z'.format(PATH_OUT, PATH_EXT), "file2"),
                 find_text('cd {}; 7z l arch1.7z'.format(PATH_OUT, PATH_EXT), "file3")]
    assert all(res_list4), 'test_step4 FAIL'


def test_step5():
    # проверка разархивирования с путями (x)
    res_list5 = [find_text('cd {}; 7z x arch1.7z -o{} -y'.format(PATH_OUT, PATH_EXT_X), "Everything is Ok"),
                 find_text('ls {}'.format(PATH_EXT_X), 'file1'),
                 find_text('ls {}'.format(PATH_EXT_X), 'file2'),
                 find_text('ls {}'.format(PATH_EXT_X), 'file3')]
    assert all(res_list5), 'test_step5 FAIL'


if __name__ == '__main__':
    pytest.main(['-vv'])
