<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html xmlns:fb="http://ogp.me/ns/fb#" style="background-color: #000000;"> <!-- workaround for Chrome white flash -->
<head>
    <meta content="text/html; charset=ISO-8859-1" http-equiv="content-type" />
<?php 
    if ($meta != "")
    {
        echo("    <meta name=\"description\" content=\"" . $meta . "\" />\n");
    } 
?>
    <title>Mixxx - <?php echo($title); ?></title>
    <META NAME="keywords" CONTENT="dj, dj software, free dj software, mixxx, dj mix, mp3 dj, mix mp3, download, crossfader, digital dj, beatmix, beatmixing, mp3, open source, mixing, mixer" />
    <link rel="shortcut icon" href="/favicon.ico" />
    <link rel="stylesheet" href="/css/mixxx1.css">
    <link href='http://fonts.googleapis.com/css?family=Muli&v1' rel='stylesheet' type='text/css'>
    <link rel="alternate" type="application/rss+xml" title="Mixxx RSS Feed" href="http://feeds.feedburner.com/MixxxNews" />
    <link href="https://plus.google.com/102441931224839455484" rel="publisher" />
    <!--[if lt IE 7.]>
    <script defer type="text/javascript" src="/js/pngfix.js"></script>
    <![endif]-->
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>  
	<?php if (function_exists("extraHead")) {
			 extraHead(); 
		  }
	?>

    <script type="text/javascript">


    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-3647499-1']);
    _gaq.push(['_trackPageview']);

    function trackDownload(url) {
      _gaq.push(['_trackPageview', url]);
    }

    (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
    </script>

<script type="text/javascript">    
    var OSName="your OS";
    if (navigator.appVersion.indexOf("Win")!=-1) OSName="Windows";
    
    // OS X why do you come in so many binary-incompatible flavours?
    if (navigator.appVersion.indexOf("Mac")!=-1) 
    {
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
    
</script>

</head>
<body>

<div id="fb-root"></div>
<script>(function(d, s, id) {
      var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
          js = d.createElement(s); js.id = id;
            js.src = "//connect.facebook.net/en_US/all.js#xfbml=1";
              fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>
