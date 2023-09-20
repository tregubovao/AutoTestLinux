import subprocess


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


def get_stdout(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    return result.stdout


if __name__ == '__main__':
    print(find_text('cat /etc/os-release', '22.04.1'))
    print(find_text('cat /etc/os-release', '22.04.8'))
    print(find_text('cat /etc/os-release', 'jammy'))
