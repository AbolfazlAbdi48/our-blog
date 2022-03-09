// intro slider
let introSlideIndex = 1

const plusIntroSlides = (n) => {
    showIntroSlides(introSlideIndex += n)
}

const showIntroSlides = (n) => {
    var introSlides = document.getElementsByClassName('intro-box')
    if (n > introSlides.length) { introSlideIndex = 1 }
    if (n < 1) { introSlideIndex = introSlides.length }
    for (let i = 0; i < introSlides.length; i++) {
        introSlides[i].classList = 'col-md-12 intro-box fade'
    }
    introSlides[introSlideIndex - 1].classList = 'col-md-12 intro-box fade show'
}

showIntroSlides(introSlideIndex)
