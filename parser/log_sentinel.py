from platform import uname, freedesktop_os_release
from os import popen

from parser.definitions import LOG_SENTINEL_DEF
class Logsentinel(LOG_SENTINEL_DEF):
    def __init__(self, data):
        super().__init__(**data)
        self.uname = uname()
        self.os = self.uname.system
        
    def select_distro(self):
        if self.os.lower().startswith("linux"):
            if "linux" in self.os.lower():
                self.distro_information = freedesktop_os_release()
                self.distro = self.distro_information["ID"].lower()
                self.distro_version = self.distro_information["VERSION_ID"]
    
    def get_log_files(self):
        if self.distro == "ubuntu":
            if self.distro_version == "24.04":
                self.FIND_FILE_COMMAND = "sudo find /var/log -type f -name \"*\" | grep -E '\\.log(\\.[0-9]+)?$' | awk '{$1=$1; print}'"
                self.ubuntu_system_log_files = popen(self.FIND_FILE_COMMAND).read().strip().split()

    def split_log_files(self):
        self.postgresql_log = [log_file for log_file in self.ubuntu_system_log_files if "postgresql" in log_file]