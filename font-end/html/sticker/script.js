const layoutWidth = 2600
const layoutHeight = 130
const totalImages = 20
const imageWidth = layoutWidth / totalImages
const imageHeight = layoutHeight
let count = 1
let positionX = 0
const stickerElement = document.querySelector('.sticker')

setInterval(function() {
  positionX = -(imageWidth * count)
  stickerElement.style.backgroundPosition = `${positionX}px 0`
  count++
  count = (count >= totalImages) ? 0 : count
}, 1000 / totalImages)