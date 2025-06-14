#! /usr/bin/python3.12

from platform import uname, freedesktop_os_release
import io

class Logsentinel():
    def __init__(self):
        self.uname = uname()
        self.os = self.uname.system

        self.select_distro()
        
    def select_distro(self):
        if self.os.lower().startswith("linux"):
            if "linux" in self.os.lower():
                self.distro_information = freedesktop_os_release()
                self.distro = self.distro_information["ID"].lower()
                self.distro_version = self.distro_information["VERSION_ID"]
                self.get_log_files()
    
    def get_log_files(self):
        """
            Ubuntu 24.04
        """
        if self.distro == "ubuntu":
            if self.distro_version == "24.04":
                self.UBUNTU_AUTH_LOG = "/var/log/auth.log"
                self.UBUNTU_DAEMON_LOG = "/var/log/daemon.log"
                self.UBUNTU_DEBUG_LOG = "/var/log/debug"
                self.UBUNTU_KERNEL_LOG = "/var/log/kern.log"
                self.UBUNTU_SYSTEM_LOG = "/var/log/syslog"

                self.ubuntu_log_files()

    def ubuntu_log_files(self):
        with open(self.UBUNTU_AUTH_LOG, 'r', encoding="UTF-8", errors="ignore") as auth_log:
            self.auth_log = [auth_log.strip() for auth_log in auth_log.readlines()]
        
        with open(self.UBUNTU_DAEMON_LOG, 'r', encoding="UTF-8", errors="ignore") as daemon_log:
            self.daemon_log = [daemon.strip() for daemon in daemon_log.readlines()]

        with open(self.UBUNTU_SYSTEM_LOG, 'r', encoding="UTF-8", errors="ignore") as sys_log:
            self.sys_log = [sys_log.strip() for sys_log in sys_log.readlines()]
            
    
    def __str__(self):
        return f"{self.os} {self.distro} {self.distro_version}"
    
if __name__ == "__main__":
    app = Logsentinel()
