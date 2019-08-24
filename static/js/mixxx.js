var OSName = getOSName();

function getOSName() {
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
