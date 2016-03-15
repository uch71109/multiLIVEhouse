
# multiLIVEhouse

multiLIVEhouse改寫自mulitiTwitch專案
提供多視窗同時觀看直播平台LIVEhouse.in的功能

## 範例網站
範例網站建立於Google App Engine
網址：http://multilivehouse.appspot.com/

## 安裝步驟
multiLIVEhouse使用Python 語言進行開發, 配合webapp2 + Jinja2, 並放置於App Engine
 * 下載 Python:
```shell
https://www.python.org/downloads/
``` 
 * 下載 App Engine SDK:
```shell
https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python
```
* 安裝Jinja2:
```shell
pip install Jinja2
```
## 使用範例
接下來可以利用App Engine提供的工具將專案進行Deploy
* 假設多視窗的頻道編號為KISSRADIO, musou1
則輸入
```shell
http://multilivehouse.appspot.com/KISSRADIO/musou1
```
* 假設多視窗的頻道編號為KISSRADIO, musou1, Haifong
則輸入
```shell
http://multilivehouse.appspot.com/KISSRADIO/musou1/Haifong
```
其他則以此類推

## Reference
* [LIVEhouse.in](https://livehouse.in/)
* [multitwitch](https://github.com/bhamrick/multitwitch)