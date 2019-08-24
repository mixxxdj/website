;(function() {
    var classToBox;
    var OSName = utils.getOSName();
    
    if (OSName.indexOf('Mac') !== -1) {
      classToBox = 'macbox';
    }
    else if (OSName.indexOf('Windows') !== -1) {
      classToBox = 'winbox';
    }
    
    if (classToBox) {
      window.setTimeout(
        utils.addClassToEls.bind(window, 'slow_border', document.getElementsByClassName(classToBox)),
        1000
      )
    }
}());
