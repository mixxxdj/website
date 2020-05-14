function setupGallery(galleryContainer, imgElement, images) {
  let imageIndex = 0;

  function setImage(indexChange) {
    imageIndex = posMod(imageIndex + indexChange, images.length);
    imgElement.src = images[imageIndex];
  }

  // start autoplay
  const intervalId = setInterval(function () { setImage(+1) }, 5000);

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
