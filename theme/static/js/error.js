(function() {
    document.addEventListener("DOMContentLoaded", function() {
        let element = document.querySelector("#error-path");
        if (element) {
            element.textContent = window.location.pathname;
        }
    });
}());
