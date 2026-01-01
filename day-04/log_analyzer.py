import json

def read_logs():
    try:
        with open("app.log", "r") as file:
            lines = file.readlines()
            if not lines:
                print("Log file is empty.")
                return []
            return lines
    except FileNotFoundError:
        print("Error: app.log not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def analyze(lines):
        log_count = {
            "INFO": 0,
            "WARNING":0,
            "ERROR":0
    }
        for line in lines:
                if "INFO" in line: 
                    log_count.update({"INFO": log_count["INFO"]+1})
                elif "WARNING" in line:
                    log_count.update({"WARNING": log_count["WARNING"]+1})
                elif "ERROR" in line:
                    log_count.update({"ERROR": log_count["ERROR"]+1})
                else:pass
        return log_count
def write_json(counts):
      with open("output.json","w+") as json_file:
          json.dump(counts,json_file)

lines = read_logs()
counts = analyze(lines)
write_json(counts)
print(counts) 