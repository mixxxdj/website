<?php 
$title = "Free MP3 DJ Mixing Software";
$meta = "Download the most advanced FREE DJ software available, featuring iTunes integration, MIDI controller support, internet broadcasting, and integrated music library.";
require('header.php'); 
?>
<?php
require('navbar.php'); 
?>

<div id="driveby_social">
    <script type="text/javascript">
    $('#driveby_social').delay(2000).fadeIn(1000);
    </script>
    <ul><li>
    <a href="https://twitter.com/share" class="twitter-share-button" data-url="http://www.mixxx.org" data-text="Check out Mixxx - Free MP3 DJ mixing software for Windows, Mac OS X, and Linux" data-via="mixxxdj" data-count="vertical">Tweet</a>
    <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
    </li>

    <li>
    <!-- Place this tag where you want the +1 button to render -->
    <g:plusone size="tall" href="http://www.mixxx.org"></g:plusone>

    <!-- Place this render call where appropriate -->
    <script type="text/javascript">
    (function() {
    var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
    po.src = 'https://apis.google.com/js/plusone.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
    })();
    </script>
    </li>

        <fb:like href="http://www.mixxx.org" send="false" layout="box_count" width="60" show_faces="false" style="position: relative; top: -4px;"></fb:like>
        <li>
        </li>
    </ul>
</div>

<div id="splash">
    <img src="/images/splash1.png" height=380 width=920>
</div>


<div id="wrapper">

<div class="gapfiller" style="margin-bottom: 0px;">
    <div class="download_button">
        <img src="/images/download.png" alt="Download Now for FREE!" onclick="location.href='/downloadlatest.php?os=' + OSName;" border="0px" style="vertical-align: middle; cursor:pointer; margin-top: -30px; margin-bottom: -30px;" />
        <!--
        <div style="padding-left: 24px; width: 192px;">
        <p>Download FREE for <script type="text/javascript"> document.write(OSName); </script> </p>
        </div>  
        -->
    </div>
    <div style="float: right; margin-top: 0px; margin-right: -14px;">
        <script type="text/javascript">
            if (OSName.search("OS X") >= 0) {
                document.write('<a href="http://itunes.apple.com/us/app/mixxx/id413756578?mt=12&ls=1"><img src="/images/available-on-mac-app-store-frontpage.png" ></a><br>');
            } else
            {
                document.write("<p><small>Download FREE for " + OSName + "</small></p>");
            }
            </script>
    </div>
    <!--
    <div style="float: right; margin-top: 16px; padding-right: 8px;">
        <img src="/images/squiggle.png">
    </div>-->
    <div style="width: 500px; padding-top: 6px;" >
        <p style="padding: 0px; margin: 0px; text-align: center;">The most advanced free DJ software <br>can be yours in seconds.
        <!--Start creating live MP3 DJ mixes today.-->
        </p>
    </div>
    <div style="clear: both;"></div>
</div> <!-- gapfiller -->
 

<div class="content">
<H1>Incredible Features, Unbeatable Value</H1>
Mixxx has everything you need to start making DJ mixes in a tight, integrated package. Whether you're DJing your next house party, spinning at a club, or broadcasting as a radio DJ, Mixxx has what you need to do it right.

<div class="halfbox_left">
    <H2><img src="/images/ic_library_itunes.png" class="feature_icon">iTunes Integration</H2>
    <p class="feature_indent">All your playlists and songs from iTunes, automatically ready to go for your next live DJ performance.
    </p>
</div>
<div class="halfbox_right">
    <H2><img src="/images/ic_preferences_controllers.png" class="feature_icon">DJ MIDI Controller Support</H2>
    <p class="feature_indent">With over 30 DJ MIDI controllers supported out-of-the-box, Mixxx gives you comprehensive hardware control for your DJ mixes.
    </p>
</div>
<div style="clear: both;"></div>
<div class="halfbox_left">
    <H2><img src="/images/ic_library_prepare.png" class="feature_icon">BPM Detection and Sync</H2>
    <p class="feature_indent">Instantly sync the tempo of two songs for seamless beatmixing. Need a break? Create a quick playlist and let Auto DJ take over.
    </p>
</div>
<div class="halfbox_right">
    <H2><img src="/images/ic_preferences_crossfader.png" class="feature_icon">Powerful Mixing Engine</H2>
    <p class="feature_indent">
    Mixxx has a cutting-edge mixing engine including support for MP3, M4A/AAC, OGG, and FLAC audio, adjustable EQ shelves, timecode vinyl control, recording, and Shoutcast broadcasting. <a href="/features">Read more</a>
    </p>
</div>
<div style="clear: both;"></div>

<div class="gapfiller" style="height: 57px;">
    <div class="download_button">
        <img src="/images/download.png" alt="Download Now for FREE!" onclick="location.href='downloadlatest.php?os=' + OSName;" border="0px" style="vertical-align: middle; cursor:pointer; margin-top: -30px; margin-bottom: -30px;" />
    </div>
<p style="text-align: center;">See <a href="/features">dozens more features</a> or start downloading Mixxx for FREE now:</a></p>
</div>

<H1>And It Just Keeps Getting Better</H1>
<p>
Each year, a community of DJs, programmers, and artists contribute dozens of new features to Mixxx. <br>
<b>And it doesn't cost you a dime.</b>
</p>
<p>Because Mixxx is <b>open source</b>, anyone can remix or add new features to it. And that includes you!</p>
<p>You can get involved with Mixxx today by <a href="/get-involved#developers">creating your own branch</a>, <a href="/get-involved#translators">helping with translations</a>, or working on one of our other <a href="/get-involved">starter tasks</a>.
</p>

<div id="achievements">
    <div class="achievement" style="width: 180px;">
    <img src="/images/rating_macappstore.png" alt="#1" style="padding-top: 10px;">
    <br>
    Top Free Mac App,<br>
    Mac App Store<br>
    <small>February 2011</small>
    </div>
    <div class="achievement">
        <img src="/images/rating_cnet.png" alt="CNet">
    </div>
    <div class="achievement">
        <img src="/images/rating_cm.png" alt="Computer Music"><br>
        Free Pick of the Month<br>
        <small>September 2007</small>
    </div>
    <div class="achievement">
        <img src="/images/rating_synthtopia.png" alt="Synthtopia" style="padding-top: 45px;">
        <br>
        "The coolest open source<br>application ever?"<br>
        <small>February 2011</small>
    </div>
    <div style="clear: both;"></div>
</div>

<H1>If you like Mixxx...</H1>
<div style="float: right;">
    <a href="http://www.oscillicious.com/?utm_source=mixxx&utm_medium=gap_banner&utm_content=frontpage_workinghard&utm_campaign=mixxx"><img src="/images/oscillicious_logo1.png"></a>
</div>
<p>The developers of Mixxx at <a href="http://www.oscillicious.com/?utm_source=mixxx&utm_medium=gap_banner&utm_content=frontpage_workinghard&utm_campaign=mixxx">Oscillicious Audio Labs</a> have been working hard on <a href="http://www.oscillicious.com/beatcleaver?utm_source=mixxx&utm_medium=gap_banner&utm_content=frontpage_workinghard&utm_campaign=mixxx">BeatCleaver</a> and <a href="http://www.oscillicious.com/sodasynth?utm_source=mixxx&utm_medium=gap_banner&utm_content=frontpage_workinghard&utm_campaign=mixxx">SodaSynth</a>, check them out!
</p>
<div style="clear: both;"></div>

</div> <!-- content -->

<?php require('footer.php'); ?>
