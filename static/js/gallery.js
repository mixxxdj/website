function setupGallery(galleryContainer, imgElements) {
  // copy the HTMLCollection to an array
  // manipulating the classList later on also affects the HTMLCollection, which we don't want
  const imgElementsArray = Array.from(imgElements);
  let imageIndex = 0;

  const computedStyle = getComputedStyle(galleryContainer);
  const originalWidth = computedStyle.getPropertyValue("--splash_img_original_width").trim().replace("px", "");
  const originalHeight = computedStyle.getPropertyValue("--splash_img_original_height").trim().replace("px", "");;

  const scaleFactor = imgElements[0].offsetWidth / originalWidth;
  const newHeight = scaleFactor * originalHeight;

  galleryContainer.style.width = imgElements[0].offsetWidth + "px";
  galleryContainer.style.height = newHeight + "px";

  for (const img of Array.from(imgElementsArray)) {
    img.classList.remove("splash_img_non_js");
    img.classList.remove("splash_img_hidden_non_js");
    img.classList.add("splash_img_with_js");

    img.style.height = newHeight + "px";
  }

  function setImage(indexChange) {
    if (indexChange != -1 && indexChange != +1) {
      throw new Error("Argument 'indexChange' must be -1 or +1!");
    }

    const oldImage = imgElementsArray[imageIndex];
    imageIndex = posMod(imageIndex + indexChange, imgElementsArray.length);
    const newImage = imgElementsArray[imageIndex];
    
    oldImage.classList.add("splash_img_hidden");
    newImage.classList.remove("splash_img_hidden");
  }

  // start autoplay
  const intervalId = 0//setInterval(function () { setImage(+1) }, 5000);

  galleryContainer.addEventListener("click", function (event) {
    clearInterval(intervalId); // stop autoplay

    const imgBoundingRect = galleryContainer.getBoundingClientRect();
    const imgCenterX = imgBoundingRect.x + imgBoundingRect.width / 2;
    const clickedOnLeftSide = event.clientX < imgCenterX;

    const changeBy = clickedOnLeftSide ? -1 : 1;
    setImage(changeBy);
  });
}

function posMod(n, m) {
  return ((n % m) + m) % m;
}
