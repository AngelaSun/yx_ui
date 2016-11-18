function connectWebViewJavascriptBridge(callback) {
    if (window.WebViewJavascriptBridge) {
        compatibleYiXinJSBridge();
        callback(WebViewJavascriptBridge)
    } else {
        document.addEventListener('WebViewJavascriptBridgeReady', function() {
                                  compatibleYiXinJSBridge();
                                  callback(WebViewJavascriptBridge)
                                  }, false)
    }
}

function compatibleYiXinJSBridge(){
    window.NEJsbridge =  window.WebViewJavascriptBridge;
    window.NEJsbridge.call = window.NEJsbridge.callHandler;

    //yixin invoke 接口申明确认下
    window.NEJsbridge.invoke = window.NEJsbridge.callHandler;

    notifyYiXinJsbridgeReadyEvent()
}

function notifyYiXinJsbridgeReadyEvent()
{
    var doc = document
    var readyEvent = doc.createEvent('Events')
    readyEvent.initEvent('NEJsbridgeReady')
    readyEvent.bridge = WebViewJavascriptBridge
    doc.dispatchEvent(readyEvent)
}


connectWebViewJavascriptBridge(function(bridge){
                               bridge.init(function(message, responseCallback) {})
                               });

//if (window.NEJsbridge)
//{
//    NEJsbridge.invoke("setShareParams", {"ab":"cd"});
//}
//else
//{
//    document.addEventListener('NEJsbridgeReady', function onBridgeReady() {
//                                NEJsbridge.invoke("setShareParams", {"ab":"cd"});
//                              });
//}
