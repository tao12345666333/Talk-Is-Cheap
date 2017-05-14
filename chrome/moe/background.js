chrome.runtime.onInstalled.addListener(function() {
  console.log(chrome);
  console.log(chrome.storage);
  chrome.storage.local.clear();
  chrome.storage.local.set({name: 'moelove.info'});
  chrome.storage.local.get('name', function(e){
    console.log(e);
  })
});

chrome.app.runtime.onLaunched.addListener(function() {
  chrome.app.window.create('window.html', {
    id: 'moelove',
    bounds: {
      width: 200,
      height: 300,
      top: 100,
      left: 200
    },
    // resizable: false,
    minWidth: 100,
    minHeight: 100
  });
});

chrome.runtime.onSuspend.addListener(function() {
});
