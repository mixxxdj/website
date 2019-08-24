;(function(utils) {

  utils.addClassToEls = function(klass, els) {
    for (var i = 0, n = els.length; i < n; i++) {
      els[i].className = els[i].className + ' ' + klass;
    }
  }

  utils.getOSName = function() {
    var OSName = "";
  
    var osToPlatformMap = {
      "Windows": ["Win"],
      "MacOS": ["Mac"],
      "Linux": ["Linux", "X11"],
    }

    for (var os in osToPlatformMap) {
      if (osToPlatformMap.hasOwnProperty(os) && navigator.appVersion.indexOf(os) !== -1) {
        OSName = os;
      }
    }
  
    return OSName;
  }
}(this.utils = this.utils || {}));
