from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/scan")
def scan(target: str):
    try:
        # Run Nmap command
        result = subprocess.check_output(
            ["nmap", "-sV", "-T4", "-oN", "-", target],
            stderr=subprocess.STDOUT
        )
        return {"target": target, "scan_result": result.decode("utf-8")}
    except subprocess.CalledProcessError as e:
        return {"error": e.output.decode("utf-8")}
