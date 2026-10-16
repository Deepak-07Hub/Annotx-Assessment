import json
import re

def extract_features(text):
    rules = {
        "hardware": ["STM32", "Raspberry Pi"],
        "software": ["FreeRTOS"],
        "protocols": ["SPI", "UART", "MQTT"],
        "languages": ["C", "Python"]
    }
    data = {k: [] for k in rules}
    
    for category, keywords in rules.items():
        for kw in keywords:
            # \b ensures we only match whole words, re.IGNORECASE makes it case-insensitive
            if re.search(rf"\b{re.escape(kw)}\b", text, re.IGNORECASE):
                data[category].append(kw)
                
    return json.dumps(data, indent=2)

if __name__ == "__main__":
    content = "The application uses an STM32 microcontroller running FreeRTOS. Sensor data is collected through SPI and processed using a moving-average filter. The processed data is sent to a Raspberry Pi over UART and published to the backend using MQTT. The firmware is primarily written in C, while Python is used for data analysis."
    print(extract_features(content))