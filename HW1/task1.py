import subprocess


def find_text(command: str, text: str) -> bool:
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if text in out and result.returncode == 0:
        return True
    return False


if __name__ == '__main__':
    print(find_text('cat /etc/os-release', '22.04.1'))
    print(find_text('cat /etc/os-release', '22.04.8'))
    print(find_text('cat /etc/os-release', 'jammy'))
