import subprocess

PATH_IN = '/home/user/AT/in'
PATH_OUT = '/home/user/AT/out'
PATH_NEW = '/home/user/AT/new'
PATH_EXT = '/home/user/AT/ext'
PATH_EXT_X = '/home/user/AT/ext-x'


def find_text(cmd: str, text: str) -> bool:
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if text in out and result.returncode == 0:
        return True
    return False


def find_text_negative(cmd: str, text: str) -> bool:
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8', stderr=subprocess.PIPE)
    out = result.stdout
    if text in out or text in result.stderr:
        return True
    return False


if __name__ == '__main__':
    print(find_text('cat /etc/os-release', '22.04.1'))
    print(find_text('cat /etc/os-release', '22.04.8'))
    print(find_text('cat /etc/os-release', 'jammy'))
