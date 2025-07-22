import json 
import sys
from security import safe_requests

def main():
    if len(sys.argv) !=2:
        sys.exit()
    
    response = safe_requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+ sys.argv[1])
    # print(json.dumps(response.json(), indent=2))

    obj = response.json()
    for result in obj["results"]:
        print(result["trackName"])

if __name__=="__main__":
    main()
