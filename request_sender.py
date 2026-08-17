import requests
import time

def send_one(payload, url, timeout=5):
    start = time.perf_counter()
    try:
        resp = requests.post(url, data={"password": payload}, timeout=timeout)
        elapsed = time.perf_counter() - start
        return {
            "payload": payload,
            "status": resp.status_code,
            "length": len(resp.content),
            "time": round(elapsed, 3),
            "error": None,
        }
    except requests.RequestException as e:
        return {"payload": payload, "status": None, "length": 0, "time": None, "error": str(e)}
