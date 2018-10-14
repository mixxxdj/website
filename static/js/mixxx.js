var OSName = getOSName();

function getOSName() {
  var OSName="your OS";
  if (navigator.appVersion.indexOf("Win")!=-1) OSName="Windows";

  // OS X why do you come in so many binary-incompatible flavours?
  if (navigator.appVersion.indexOf("Mac")!=-1) {
    OSName="Mac OS X";
    if ((navigator.userAgent.indexOf("10.5") != -1) //Leopard, Firefox
        || (navigator.userAgent.indexOf("10_5") != -1)) //Leopard, Webkit
    {
      OSName += " 10.5";
    }
    else if ((navigator.userAgent.indexOf("10.4") != -1) //Tiger, Firefox
             || (navigator.userAgent.indexOf("10_4") != -1)) //Tiger, Webkit
    {
      OSName += " 10.4";
    }

    if (navigator.userAgent.indexOf("Intel Mac")!=-1) //Intel machines
    {
      //OSName += " (Intel)";
      OSName += " (Intel)";
    }
  }

  if (navigator.appVersion.indexOf("X11")!=-1) OSName="Linux";
  if (navigator.appVersion.indexOf("Linux")!=-1) OSName="Linux";

  return OSName;
}
