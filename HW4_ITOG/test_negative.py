from sshcheckers import ssh_checkout_negative
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)


class TestNegative:

    def test_n_step1(self, make_folders, bad_arch):
        assert ssh_checkout_negative(data["IP_address"], data["user"], data["passwd"],
                                     f'cd {data["folder_out"]}; 7z e {bad_arch}.{data["type"]} -o{data["folder_ext"]} -y',
                                     "ERROR:"), "test1 FAIL"

    def test_n_step2(self, bad_arch):
        assert ssh_checkout_negative(data["IP_address"], data["user"], data["passwd"],
                                     f'cd {data["folder_out"]}; 7z t {bad_arch}.{data["type"]}', "ERROR:"),\
                                        "test2 FAIL"

