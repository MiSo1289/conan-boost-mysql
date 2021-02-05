import os

from conans import ConanFile, CMake, tools


class BoostMysql(ConanFile):
    name = "boost_mysql"
    version = "1.75.0"
    revision_mode = "scm"
    url = "https://github.com/anarthal/mysql"
    license = "BSL-1.0"

    source_subfolder = "sources"
    scm = {
        "type": "git",
        "url": url,
        "subfolder": source_subfolder,
        "revision": "master",
    }

    def package(self):
        self.copy("*.hpp", dst="include", src=os.path.join(source_subfolder, "include"))

    def package_id(self):
        self.info.header_only()
