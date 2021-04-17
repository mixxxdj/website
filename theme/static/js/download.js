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
            return ["windows", "win" + detectBitness()];
        }
        if (window.navigator.userAgent.indexOf("Mac") !== -1) {
            return ["macos", ["macosintel"]];
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

    let expandAccordionByHash = function() {
        if (document.location.hash) {
            let anchorButton = document.querySelector(".accordion " + location.hash + " > input.expander");
            if (anchorButton) {
                anchorButton.checked = true;

                // Re-scoll to anchor (works around wrong scroll position
                // caused by the accordion changes *after* we already scrolled).
                let section = document.querySelector(".accordion " + location.hash)
                if (section) {
                    section.scrollIntoView();
                }
            }
        }
    }

    let updateDownloadButton = function() {
        let os = detectOS();
        if (os === null) {
            return;
        }

        // Update the "Download" button at the top of the page
        let button = document.querySelector("#download .download-button")
        if (!button) {
            return;
        }

        let description = document.querySelector("#download .download-button-description")
        if (!description) {
            return;
        }

        console.log("OS", os);

        let osName = os[0];
        let osArch = os[1];

        // Check if we can find a direct package download. If so, make the
        // download button download it.
        let packageNotFound = osArch.every(function(dlName) {
            let package = document.querySelector("#stable .download-" + osName + " .package-" + dlName)
            console.log("#stable .download-" + osName + " .package-" + dlName)
            console.log(package)
            console.log(package.href)
            console.log(package.dataset.os)
            if (!package || !package.href || !package.dataset.os) {
                // This is equivalent to a for loop's "continue"
                return true;
            }

            button.href = package.href;
            button.innerHTML = button.dataset.osdetectText.replace("%s", package.dataset.os);
            description.innerHTML = description.dataset.osdetectText;
            return false;
        });

        // Array.every(callback) returns true if callback returned true for
        // each value *or* if the array was empty.
        if (!packageNotFound) {
            return;
        }

        // We didn't find a matching package to download. Check if there is a
        // matching download section and make the button scroll to it.
        let input = document.querySelector("#stable .download-" + osName + " input.expander");
        if (!input) {
            return;
        }

        let section = input.parentNode;
        if (section || section.id || section.dataset.os) {
            button.href = "#" + section.id;
            button.innerHTML = button.dataset.osdetectText.replace("%s", section.dataset.os);
            description.innerHTML = description.dataset.osdetectText;
        }
    }

    window.addEventListener('hashchange', expandAccordionByHash);
    document.addEventListener("DOMContentLoaded", expandAccordionByHash);
    document.addEventListener("DOMContentLoaded", updateDownloadButton);
}());
