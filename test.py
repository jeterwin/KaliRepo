import subprocess

subprocess.run("./hehe.exe", creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
#MERGE - subprocess.Popen(["python", "hehe.py"], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_NO_WINDOW | subprocess.DETACHED_PROCESS,
                 #stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

#subprocess.Popen(["python", "hehe.py"], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
# MERGE - subprocess.run(["attrib","+h",".\hehe2.py"], check=True)