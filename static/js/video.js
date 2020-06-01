document.addEventListener("DOMContentLoaded", function() {
    // Your code to run since DOM is loaded and ready
    for (let element of document.querySelectorAll(".video-container")) {
        let dialog = document.querySelector(".video-dialog");
        let video_id = dialog.dataset.source;
        let button = element.querySelector(".video-button");
        button.addEventListener("click", function() {
            let iframe = document.createElement("iframe");
            iframe.src = "https://www.youtube-nocookie.com/embed/" + video_id + "?rel=0&controls=0&showinfo=0&autoplay=1&mute=1";
            dialog.style.display = "none";
            element.appendChild(iframe);
        });
        button.style.display = "inline-block";
    }
});
