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
                return ["64", "32"];
            }
        }
        return ["32"];
    }

    let detectOS = function () {
        if (window.navigator.userAgent.indexOf("Windows") !== -1) {
            return ["windows", detectBitness()];
        }
        if (window.navigator.userAgent.indexOf("Mac") !== -1) {
            return ["macos", ["intel"]];
        }
        if (window.navigator.userAgent.indexOf("Ubuntu") !== -1) {
            return ["ubuntu", []];
        }
        if (window.navigator.userAgent.indexOf("Fedora") !== -1) {
            return ["fedora", []];
        }
        if (window.navigator.userAgent.indexOf("Arch Linux") !== -1) {
            return ["archlinux", []];
        }
        return null;
    }

    let os = detectOS();
    if (os === null) {
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

        let osName = os[0];
        let osArch = os[1];

        // Check if we can find a direct package download. If so, make the
        // download button download it.
        let packageFound = osArch.every(function(item) {
            let dlName = osName + osArch;

            let package = document.querySelector("#stable .download-" + osName + " .package-" + dlName)
            if (!package || !package.href || !package.dataset.os) {
                // This is equivalent to a for loop's "continue"
                return true;
            }

            button.href = package.href;
            if (package.onclick) {
                button.setAttribute("onclick", package.onclick.toString());
            }
            button.innerHTML = button.dataset.osdetectText.replace("%s", package.dataset.os);
            description.innerHTML = description.dataset.osdetectText;
            return false;
        });

        // Array.every(callback) returns true if callback returned true for
        // each value *or* if the array was empty.
        if (packageFound && osArch.length > 0) {
            return;
        }

        // We didn't find a matching package to download. Check if there is a
        // matching download section and make the button scroll to it.
        let input = document.querySelector("#stable .download-" + osName);
        if (!input) {
            return;
        }

        let section = input.parentNode;
        if (section || section.id || section.dataset.os) {
            button.href = "#" + section.id;
            button.innerHTML = button.dataset.osdetectText.replace("%s", section.dataset.os);
            description.innerHTML = description.dataset.osdetectText;
            input.checked = true;
        }
    });
}());
