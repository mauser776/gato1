/* Created by Tivotal */

var swiper = new Swiper(".slider-content", {
  slidesPerView: 4,
  spaceBetween: 25,
  loop: true,
  centerSlide: true,
  fade: true,
  grabCursor: true,
  // pagination: {
  //   el: ".slider .swiper-pagination",
  //   clickable: true,
  //   dynamicBullets: true,
  // },
  navigation: {
    nextEl: "#slider01 .swiper-button-next",
    prevEl: "#slider01 .swiper-button-prev",
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    520: {
      slidesPerView: 2,
    },
    950: {
      slidesPerView: 3,
    },
    1100: {
      slidesPerView: 4,
    },
    // 1100: {
    //   slidesPerView: 5,
    // },
  },
});

var swiper = new Swiper(".slider-content2", {
  slidesPerView: 3,
  spaceBetween: 25,
  loop: true,
  centerSlide: true,
  fade: true,
  grabCursor: true,
  // pagination: {
  //   el: ".slider .swiper-pagination",
  //   clickable: true,
  //   dynamicBullets: true,
  // },
  navigation: {
    nextEl: "#slider02 .swiper-button-next",
    prevEl: "#slider02 .swiper-button-prev",
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    520: {
      slidesPerView: 2,
    },
    950: {
      slidesPerView: 3,
    },
    // 1100: {
    //   slidesPerView: 4,
    // },
  },
});


