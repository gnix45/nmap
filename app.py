from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/scan")
def scan(target: str):
    try:
        # Use connect scan instead of raw sockets
        result = subprocess.check_output(
            ["nmap", "-sT", "-Pn", "-p", "1-1000", "-T4", "-oN", "-", target],
            stderr=subprocess.STDOUT
        )
        return {"target": target, "scan_result": result.decode("utf-8")}
    except subprocess.CalledProcessError as e:
        return {"error": e.output.decode("utf-8")}
