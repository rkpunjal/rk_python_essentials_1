
# Online Package ist www.pypi.org
# cmd : pip list

import os
import sys
# import pkg_resources
#
#
# def print_installed_packages():
#     print("Installed Packages: ")
#     print("---------------------")
#     installed_packages = pkg_resources.working_set
#     for package in installed_packages:
#         print(f"{package.key}=={package.version}")


print("---------------------")
print("Operating System : ", os.name)
print("---------------------")
print("Python version : ", sys.version, "(", sys.version_info, ")")
print("---------------------")
# print_installed_packages()

