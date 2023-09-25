from sshcheckers import ssh_checkout, upload_files
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)


class TestPositive:

    def test_step1_deploy(self):
        res = []
        upload_files(data['IP_address'], data['user'], data['passwd'],
                     f"/home/user/PycharmProjects/pythonProject/4/tests/{data['package_name']}",
                     f"/home/user2/{data['package_name']}")
        res.append(ssh_checkout(data['IP_address'], data['user'], data['passwd'],
                                f"echo '11' | sudo -S dpkg -i /home/user2/{data['package_name']}",
                                "Настраивается пакет"))
        res.append(ssh_checkout(data['IP_address'], data['user'], data['passwd'],
                                "echo '11' | sudo -S dpkg -s p7zip-full",
                                "Status: install ok installed"))
        assert res

    def test_step1(self, make_folders, make_files):
        assert (ssh_checkout(data['IP_address'], data['user'], data['passwd'],
                             f"cd {data['folder_in']}; 7z a {data['folder_out']}/arch1 -t{data['type']}",
                             "Everything is Ok"))


    













