
import json
from urllib.request import urlopen
from urllib.parse import urlencode
from pprint import pprint
def main():
        appkey="509e7b45fabab2432bc58127ee77525f"
        request(appkey,"美元人民币")

def request(appkey,currency,m="GET"):
        
        url = "http://web.juhe.cn:8080/finance/exchange/frate"
        params = {
        "key" : appkey, #APP Key
        "type" : "0", #两种格式(0或者1,默认为0)
        }
        params=urlencode(params)
        if m=="GET":
            f=urlopen("%s?%s" % (url,params))
        else :
            f=urlopen(url,params)

        content=f.read()
        res=json.loads(content)
        if res:
             error_code=res["error_code"]
             if error_code==0:
                 for data in res["result"]:
                     results=data.values()
                     for result in results:
                         if result["currency"]==currency:
                             print("{}:{}".format(result["currency"],result["buyPic"]))

             else:
                 pprint("%s:%s" % (res["error_code"],res["reason"]))                
        else:
            pprint("request api error")
            
if __name__=="__main__":
        main()       
