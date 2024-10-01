import subprocess

# subprocess.run(["powershell", "pwd"], shell=True)

# Capture the output of a command
result = subprocess.run(["powershell", "dir", "c:\\rkData"], capture_output=True, text=True)
# result = subprocess.run(["powershell", "echo", "'Hello World!'"], capture_output=True, text=True)


print(result.stdout)
#
subprocess.Popen('echo "Yohooo!!"', shell=True)

# executing another python program
# subprocess.Popen('python --version"', shell=True)
subprocess.run(["powershell", "pwd"], shell=True)
subprocess.run(["powershell", "python", "--version"], shell=True)
subprocess.run(["powershell", "python", "./68_template_jinja2.py"], shell=True)


