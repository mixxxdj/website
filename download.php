<?php
$title = "Download the Best Free MP3 DJ Mixing Software";
$meta = "Download the most advanced FREE DJ software available, featuring iTunes integration, MIDI controller support, internet broadcasting, and integrated music library.";

function extraHead()
{
    echo <<<EOF
	<script type="text/javascript">
	/* <![CDATA[ */
	    (function() {
		var s = document.createElement('script'), t = document.getElementsByTagName('script')[0];
		s.type = 'text/javascript';
		s.async = true;
		s.src = 'http://api.flattr.com/js/0.6/load.js?mode=auto';
		t.parentNode.insertBefore(s, t);
	    })();
	/* ]]> */
	</script>
EOF;
};

require('header.php');
?>
<?php
require('navbar.php');
?>

<script type="text/javascript">
$(document).ready(function() {
    if (OSName.search("OS X") >= 0) {
        var highlightTimerId = window.setTimeout(function() { $('#macbox').addClass('slow_border');}, 1000);
    }
    else if (OSName.search("Windows") >= 0) {
        var highlightTimerId = window.setTimeout(function() { $('#winbox').addClass('slow_border');}, 1000);
    }
});
</script>

<div id="wrapper">

<div class="content">
<div style="float: right; width: 100px; padding-top: 30px;">
		  <center>
		    <form action="https://www.paypal.com/cgi-bin/webscr" method="post">
		      <input type="hidden" name="cmd" value="_s-xclick"/>
		      <input type="image" src="https://www.paypal.com/en_GB/i/btn/btn_donate_LG.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online."/>
		      <img alt="" border="0" src="https://www.paypal.com/en_GB/i/scr/pixel.gif" width="1" height="1"/>
		      <input type="hidden" name="encrypted" value="-----BEGIN PKCS7-----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-----END PKCS7-----"/>
		    </form>
		    <!--
			<a href="http://www.pledgie.com/campaigns/13624" style="margin-left: 1em; margin-right: 1em;"><img alt="Click here to lend your support to: Mixxx 1.9 Build Server Fundraiser and make a donation at www.pledgie.com !" border="0" src="http://www.pledgie.com/campaigns/13624.png?skin_name=chrome" /></a>
			-->
		  </center>
</div>
<H1>Download Now</H1>
Mixxx is available for Windows, Mac OS X, and Linux:
<div style="clear: both;"></div>
<div class="halfbox_left darkborder" id="winbox">
    <H2><img src="/images/download_windows.png" class="feature_icon">Windows</H2>
    <p>
        <a href="http://downloads.mixxx.org/mixxx-1.10.1/mixxx-1.10.1-win32.exe"
           onClick="javascript: pageTracker._trackPageview('/downloads/1.10.1win32'); ">
        Download Mixxx 1.10.1 for 32-bit Windows</a>
    </p>
    <p>
		<a href="http://downloads.mixxx.org/mixxx-1.10.1/mixxx-1.10.1-win64.exe"
		   onClick="javascript: pageTracker._trackPageview('/downloads/1.10.1win64'); ">
        Download Mixxx 1.10.1 for 64-bit Windows</a>
    </p>
    <br>
    <p><small>AAC playback requires Windows 7 or greater.</small></p>
</div>
<div class="halfbox_right darkborder" id="macbox">
    <H2><img src="/images/download_mac.png" class="feature_icon" style="margin-top: -7px;">Mac OS X</H2>
    <p>
		<a href="http://downloads.mixxx.org/mixxx-1.10.1/mixxx-1.10.1-macintel32.dmg"
		   onClick="javascript: pageTracker._trackPageview('/downloads/1.10.1osxintel'); ">
        Download Mixxx 1.10.1 for Mac OS X 10.5+ (Intel)</a>
    </p>
    <p>
		<a href="http://downloads.mixxx.org/mixxx-1.10.1/mixxx-1.10.1-macuniversal.dmg"
		   onClick="javascript: pageTracker._trackPageview('/downloads/1.10.1osxuniversal'); ">
        Download Mixxx 1.10.1 for Mac OS X 10.5+ (PPC/Intel Universal)</a>
    </p>
    <div style="text-align: center;">
 <a href="http://itunes.apple.com/us/app/mixxx/id413756578?mt=12&ls=1"><img src="/images/available-on-mac-app-store-frontpage.png" style="padding-bottom: 5px;"></a>
 </div>
    <p><small>Please note due to licensing restrictions, vinyl control is not available in Mixxx
              from the Mac App Store.</small></p>
</div>
<div style="padding: 20px;">
<H2><img src="/images/download_ubuntu.png" class="feature_icon">Ubuntu</H2>
    <p>Download Mixxx 1.10.1 for Ubuntu 10.04 (Lucid) through 12.04 (Precise):</p>
	  <p>Open a terminal, and enter:</p>
	  <pre>
	    sudo add-apt-repository ppa:mixxx/mixxx
	    sudo apt-get update
	    sudo apt-get install mixxx libportaudio2
	  </pre>
	  <p>This will install the latest version of Mixxx from
	  the <a href="https://launchpad.net/~mixxx/+archive/mixxx">Mixxx
	    PPA</a> on Launchpad.</p>
    <div style="width: 66%; margin: 0 auto;">
    <small><b>Ubuntu Repositories:</b><br/> Ubuntu also provides a version of Mixxx
	  which can be installed directly from the Ubuntu Software
	  Centre. This version is usually woefully out of date; therefore
	  using the PPA is preferable. </small>
      </div>
<H2>Linux / Source Code</H2>
    <p>
		<a href="http://downloads.mixxx.org/mixxx-1.10.1/mixxx-1.10.1-src.tar.gz"
		    onClick="javascript: pageTracker._trackPageview('/downloads/1.10.1linuxsrc'); ">
        Download Mixxx 1.10.1 Source Code
        </a>
    </p>
    <p>
		  The Mixxx source code is made available under the GPL v2. Please check the LICENSE file
		  in our source tree for complete licensing information. The latest code from Mixxx's trunk           can be downloaded through Bazaar:
		    <pre>        bzr branch lp:mixxx</pre>
    </p>
    <p>
          Compilation instructions are available for <a href="http://mixxx.org/wiki/doku.php/compiling_on_windows">Windows</a>, <a href="http://mixxx.org/wiki/doku.php/compiling_on_os_x">Mac OS X</a>, and <a href="http://mixxx.org/wiki/doku.php/compiling_on_linux">Linux</a>.
    </p>
</div>

<div class="gapfiller" style="height: 57px">
    <div style="float: right;" >
        <a href="http://www.oscillicious.com/?utm_source=mixxx&utm_medium=gap_banner&utm_content=downloads_moresoftware&utm_campaign=mixxx"><img src="/images/oscillicious_logo1.png"></a>
     </div>
    <p style="text-align: center;">More software from the Mixxx Developers available at:</p>
    <div style="clear: both;"></div>
</div>

<H2>Errata</H2>
<p>Source code for the Mac App Store version is available in each release branch in Bazaar. A
<a href="http://downloads.mixxx.org/mess/mixxx-1.9.1-macintel-appstore.dmg">corresponding binary</a> is also available.</p>

<?php require('footer.php'); ?>
