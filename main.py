#! /usr/bin/python3.12

from platform import uname, freedesktop_os_release


class Logsentinel():
    def __init__(self):
        self.uname = uname()
        self.os = self.uname.system

        self.__select_distro()
        
    def __select_distro(self):
        if self.os.lower().startswith("linux"):
            if "linux" in self.os.lower():
                # {'NAME': 'Ubuntu', 'ID': 'ubuntu', 'PRETTY_NAME': 'Ubuntu 24.04.2 LTS', 'VERSION_ID': '24.04', 'VERSION': '24.04.2 LTS (Noble Numbat)', 'VERSION_CODENAME': 'noble', 'ID_LIKE': 'debian', 'HOME_URL': 'https://www.ubuntu.com/', 'SUPPORT_URL': 'https://help.ubuntu.com/', 'BUG_REPORT_URL': 'https://bugs.launchpad.net/ubuntu/', 'PRIVACY_POLICY_URL': 'https://www.ubuntu.com/legal/terms-and-policies/privacy-policy', 'UBUNTU_CODENAME': 'noble', 'LOGO': 'ubuntu-logo'}
                self.distro_information = freedesktop_os_release()
                self.distro = self.distro_information["ID"]
                self.distro_version = self.distro_information["VERSION_ID"]
    
    def __str__(self):
        return f"{self.os} {self.distro} {self.distro_version}"
    
if __name__ == "__main__":
    app = Logsentinel()
    print(app)
