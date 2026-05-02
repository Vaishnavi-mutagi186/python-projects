import requests
import urllib3
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print("\n WEBSITE ANALYZER TOOL ")

url = input("\nEnter website URL: ")

# Auto add https
if not url.startswith("http"):
    url = "https://" + url

try:
    start = time.time()
    response = requests.get(url, timeout=5, verify=False)
    end = time.time()

    response_time = round(end - start, 2)

    print("\n==============================")
    print("Website:", url)
    print("Status Code:", response.status_code)
    print("Speed:", response_time, "sec")

    # Performance rating
    if response_time < 1:
        print(" Performance: VERY FAST")
    elif response_time < 3:
        print(" Performance: MODERATE")
    else:
        print("Performance: SLOW")

    # Status meaning
    if response.status_code == 200:
        print("✅ Status: SUCCESS (Website is working)")
    elif response.status_code == 404:
        print("❌ Status: PAGE NOT FOUND")
    elif response.status_code == 500:
        print("⚠️ Status: SERVER ERROR")
    else:
        print("⚠️ Status: UNKNOWN ISSUE")

    print("==============================\n")

except requests.exceptions.ConnectionError:
    print("❌ ERROR: No Internet Connection")

except requests.exceptions.Timeout:
    print("ERROR: Request Timed Out")

except:
    print("❌ ERROR: Invalid URL")