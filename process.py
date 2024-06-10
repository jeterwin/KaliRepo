import subprocess

subprocess.Popen(["python", "hehe.py"], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)