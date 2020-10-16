# Main module

# import http.client
from pprint import pprint
import requests

if __name__ == '__main__':

    # h = http.client.HTTPConnection('192.168.3.19', 7778)
    # h.request('GET', '/prometheus_metrics/sessions')
    # resp = str(h.getresponse().read())
    # sl = resp.split('\\n')
    # for s in sl:
    #     print(s)
    # print(sl)

    # resp = requests.request('GET', 'http://192.168.3.19:7778/prometheus_metrics/sessions')
    # print(resp)
    # print("------------------------------------")
    # sl = resp.text.split('\n')
    # for s in sl:
    #     print(s)
    # print("------------------------------------")

    # resp = requests.get('http://httpbin.org/get')
    # pprint(resp.json())

    headers = {
        "Content-type": "application/json",
        "MySecretHeader": "Balls and eggs! :)"
    }

    data = {
        "Tolyan": "Is a cool man! :)!",
        "What?": "forty two of course!"
    }

    resp = requests.post('http://httpbin.org/post', headers=headers, json=data)
    pprint(resp.json())
    print("-----------------------------")
    pprint(resp.json()["json"])
