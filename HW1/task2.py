import subprocess
import string


def find_text(command: str, text: str) -> bool:
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    for el in string.punctuation:
        out = out.replace(el, ' ')
    my_list = out.split()
    if text in my_list and result.returncode == 0:
        return True
    return False


if __name__ == '__main__':
    print(find_text('cat /etc/os-release', 'Ubuntu'))
    print(find_text('cat /etc/os-release', 'VERSION'))
    print(find_text('cat /etc/os-release', 'legal'))

