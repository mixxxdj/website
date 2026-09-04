// banner rotation with text banners trying to stay as close as possible to the original design,
// social icons only on homebanner

(function() {
    "use strict";

    console.log("🔍 Banner rotation script loaded - waiting for DOM...");

    const initBanner = function() {
        console.log("🔍 DOM ready, initializing banner...");

        const banners = [
            {
                type: "text",
                main: "DJ Your Way",
                subtitle: "Free and open source DJ software for Windows, macOS, and Linux",
                url: "/",
                target: "_self"
            },
            {
                type: "text",
                main: "Version 2.5.6 available for download",
                subtitle: "latest stable release",
                url: "https://mixxx.org/download/",
                target: "_self"
            },
            {
                type: "text",
                main: "25ᵗʰ Anniversary Artist T-Shirts available",
                subtitle: "order your exclusive T-Shirts now in our shop.",
                url: "https://shop.mixxx.org",
                target: "_blank"
            },
            {
                type: "text",
                main: "25ᵗʰ Anniversary Intergalactic DJ Contest",
                subtitle: "Submit your video before September 30th",
                url: "https://mixxx.org/news/2026-08-23-25_years_of_mixxx_dj_contest/",
                target: "_blank"
            }
        ];

        const bannerContent = document.getElementById("bannerContent");
        const bannerLink = document.getElementById("bannerLink");
        const dotsContainer = document.getElementById("bannerDots");
        const bannerContainer = document.getElementById("bannerRotation");
        const socialIcons = document.getElementById("socialIcons");

        if (!bannerContent || !bannerLink || !dotsContainer || !bannerContainer || !socialIcons) {
            console.error("Required elements not found!");
            return;
        }

        console.log("All DOM elements found!");

        let currentIndex = 0;
        let stepCounter = 0;
        let intervalId = null;
        let isPaused = false;

        const createDots = function() {
            dotsContainer.innerHTML = "";
            banners.forEach(function(_, index) {
                const dot = document.createElement("span");
                dot.className = "dot" + (index === 0 ? " active" : "");
                dot.dataset.index = index;
                dot.addEventListener("click", function(e) {
                    e.stopPropagation();
                    const idx = parseInt(this.dataset.index, 10);
                    if (idx !== currentIndex) {
                        goToBanner(idx);
                    }
                });
                dotsContainer.appendChild(dot);
            });
        };

        const updateBanner = function(index) {
            const banner = banners[index];
            bannerContent.innerHTML = "";
            const textDiv = document.createElement("div");
            textDiv.className = "banner-text";

            const mainSpan = document.createElement("span");
            mainSpan.textContent = banner.main;
            textDiv.appendChild(mainSpan);

            if (banner.subtitle) {
                const subSpan = document.createElement("span");
                subSpan.className = "subtitle";
                subSpan.textContent = banner.subtitle;
                textDiv.appendChild(subSpan);
            }

            bannerContent.appendChild(textDiv);
            bannerLink.href = banner.url;
            bannerLink.target = banner.target || "_self";
            document.querySelectorAll(".dot").forEach(function(dot, i) {
                dot.classList.toggle("active", i === index);
            });
            if (index === 0) {
                socialIcons.classList.remove("hidden");
                socialIcons.style.display = "flex";
            } else {
                socialIcons.classList.add("hidden");
                socialIcons.style.display = "none";
            }
            currentIndex = index;
        };

        const getNextBanner = function() {
            if (stepCounter % 2 === 0) {
                const bannerNumber = Math.floor(stepCounter / 2) + 1;
                return (bannerNumber % (banners.length - 1)) + 1;
            }
            return 0;
        };

        const nextBanner = function() {
            const nextIndex = getNextBanner();
            updateBanner(nextIndex);
            stepCounter = (stepCounter + 1) % (2 * (banners.length - 1));
        };

        const goToBanner = function(index) {
            updateBanner(index);
            if (index === 0) {
                stepCounter = 0;
            } else {
                stepCounter = (index - 1) * 2 + 1;
            }
            stopRotation();
            if (!isPaused) startRotation();
        };

        const startRotation = function(intervalMs) {
            intervalMs = intervalMs || 5000;
            if (intervalId) clearInterval(intervalId);
            intervalId = setInterval(nextBanner, intervalMs);
        };

        const stopRotation = function() {
            if (intervalId) {
                clearInterval(intervalId);
                intervalId = null;
            }
        };

        createDots();
        updateBanner(0);
        stepCounter = 0;
        startRotation(5000);

        bannerContainer.addEventListener("mouseenter", function() {
            isPaused = true;
            stopRotation();
        });

        bannerContainer.addEventListener("mouseleave", function() {
            isPaused = false;
            if (!intervalId) startRotation(5000);
        });

        document.addEventListener("visibilitychange", function() {
            if (document.hidden) {
                stopRotation();
            } else if (!isPaused && !intervalId) {
                startRotation(5000);
            }
        });

        console.log("Mixxx banner rotation active!");
    };

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initBanner);
    } else {
        initBanner();
    }
})();
