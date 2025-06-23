#! /usr/bin/python3.12

# LIBRARY IMPORT
from platform import uname, freedesktop_os_release
from os import popen, system

class SLOGPARSER():
    def __init__(self, path: str, log_file_type: str = "", buffer: int = -1):
        self.path = path
        self.log_file_type = log_file_type
        self.buffer = buffer

class Logsentinel():
    def __init__(self):
        self.uname = uname()
        self.os = self.uname.system
        self.BUFFERING = 1000

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
            Ubuntu 24.04 sistemleri için gerekli olan fonksiyon
            Direkt olarak sistem içerisindeki log dosyalarını alıyor.
        """
        if self.distro == "ubuntu":
            if self.distro_version == "24.04":
                self.LOG_PATH = "/var/log/"

                # INFO
                # log klasörü altındaki tüm log dosyalarını almak dosyaları alıyoruz.
                # Sembolik linkleri almadan sadece dosyaları
                # Şimdilik plan full path'ı alıp ls ile dosya özelliklerine bakmak? Sebebi yok ama
                self.FIND_FILE_COMMAND = "sudo find /var/log -type f -name \"*\" | grep -E '\\.log(\\.[0-9]+)?$' | awk '{$1=$1; print}'"

                system(self.FIND_FILE_COMMAND)
                self.ubuntu_system_log_files = popen(self.FIND_FILE_COMMAND).read().strip().split()
                
    
    def __str__(self):
        return f"{self.os} {self.distro} {self.distro_version}"
