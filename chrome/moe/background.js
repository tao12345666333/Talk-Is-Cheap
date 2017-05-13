chrome.runtime.onInstalled.addListener(function() {
  chrome.storage.local.set('', function() {
  });
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
    minWidth: 100,
    minHeight: 100
  });
});

chrome.runtime.onSuspend.addListener(function() {
});
