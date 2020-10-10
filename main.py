# Main module

import http.client

if __name__ == '__main__':

    h = http.client.HTTPConnection('192.168.3.19', 7778)
    h.request('GET', '/prometheus_metrics/sessions')
    resp = str(h.getresponse().read())
    sl = resp.split('\\n')
    for s in sl:
        print(s)
    print(sl)
