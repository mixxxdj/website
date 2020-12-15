;(function() {
    let detectBitness = function() {
        // Detect is OS is 64 bit
        const indicators64Bit = [
            "x86_64",
            "x86-64",
            "Win64",
            "x64;", // Mind the semicolon! Without it you will have false-positives.
            "amd64",
            "AMD64",
            "WOW64",
            "x64_64",
        ];
        for (let needle in indicators64Bit) {
            if (window.navigator.appVersion.indexOf(needle) !== -1) {
                return "64";
            }
        }
        return "32";
    }

    let detectOS = function () {
        if (window.navigator.userAgent.indexOf("Windows") !== -1) {
            return "windows" + detectBitness();
        }
        //if (window.navigator.userAgent.indexOf("Ubuntu") !== -1) {
        //    return "ubuntu" + detectBitness();
        //}
        if (window.navigator.userAgent.indexOf("Mac") !== -1) {
            return "osxintel";
        }
        return "unknown";
    }

    let osName = detectOS();
    if (osName === "unknown") {
        return;
    }

    document.addEventListener("DOMContentLoaded", function() {
        let button = document.querySelector("#download .download-button")
        if (!button) {
            return;
        }

        let description = document.querySelector("#download .download-button-description")
        if (!description) {
            return;
        }

        let link = document.querySelector("#stable .download-" + osName)
        if (!link || !link.href || !link.dataset.os) {
            return;
        }

        button.href = link.href;
        if (link.onclick) {
            button.setAttribute("onclick", link.onclick.toString());
        }
        description.innerHTML = link.dataset.os;
    });
}());
