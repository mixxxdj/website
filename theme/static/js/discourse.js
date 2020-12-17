;(function() {
    document.addEventListener("DOMContentLoaded", function() {
        let element = document.querySelector("#discourse-comments");
        if (!element || !element.dataset.discourseUrl || !element.dataset.discourseEmbedUrl) {
            return;
        }

        let embedUrl = element.dataset.discourseEmbedUrl;
        if (embedUrl.startsWith("/")) {
            embedUrl = location.origin + embedUrl;
        }

        window.DiscourseEmbed = {
          discourseUrl: element.dataset.discourseUrl,
          discourseEmbedUrl: embedUrl,
        };

        (function() {
            var d = document.createElement("script");
            d.type = "text/javascript";
            d.async = true;
            d.src = DiscourseEmbed.discourseUrl + 'javascripts/embed.js';
            (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(d);
        })();
    });
}());
