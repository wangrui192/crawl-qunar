### 组成
* 机票价格接口监控
* 下单模块
### 接口监控模块
* https://flight.qunar.com/twell/longwell?http%3A%2F%2Fwww.travelco.com%2FsearchArrivalAirport=%E6%88%90%E9%83%BD&http%3A%2F%2Fwww.travelco.com%2FsearchDepartureAirport=%E4%B8%8A%E6%B5%B7&http%3A%2F%2Fwww.travelco.com%2FsearchDepartureTime=2018-02-12&http%3A%2F%2Fwww.travelco.com%2FsearchReturnTime=2018-02-12&locale=zh&nextNDays=0&searchLangs=zh&searchType=OneWayFlight&tags=1&mergeFlag=0&xd=f1515129059479&wyf=isPZwPNuLsZ4hKNLL8aDPcNuisx4SsNEysc4h2U9xH2ZTcN9y2%3D%3D%3D%3D%3D%3D%7C1515124819337&ex_track=&from=qunarindex&isNewInterface=true
* 分析价格，如果存在心仪的价格，则system("python /mnt/hgfs/a.py");启动下单模块。
* 为何不接口直接下单，接口token太复杂，还有js加密，难以解决。
* 邮件通知模块。
* 监控频率，一分钟一次。
```
*/1 * * * *    nofuyun    export DISPLAY=:0 && php /mnt/hgfs/a.php
```
### 下单模块
* 使用python selenium包。浏览器配套使用Chromium。注意浏览器版本和驱动版本。
* https://www.processon.com/view/link/5a4f16c4e4b0abe85d3e08d0
