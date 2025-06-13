import os
import threading
import time
from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/")
def health():
    return "OK", 200

def run_health():
    app.run(host="0.0.0.0", port=8080)

def run_main():
    # 替换成你要执行的命令，比如启动 ArgoSB 主程序
    subprocess.run(["/ArgoSB/argosb.sh"])  # 示例路径

if __name__ == "__main__":
    t = threading.Thread(target=run_health)
    t.start()
    run_main()
