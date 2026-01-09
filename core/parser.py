import json

def analyze_json(data):

    findings_presenti = []

    for finding in data["findings"]:
            
            required = ["type","header","endpoint","severity"]

            if all(k in finding for k in required):
                finding["type"] = finding["type"].strip()
                finding["header"] = finding["header"].strip()
                finding["severity"] = finding["severity"].strip().upper()
                findings_presenti.append(finding)
            else:
                continue

    return findings_presenti