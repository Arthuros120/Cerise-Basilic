window.addEventListener('scroll' , () => {
    const subnav = document.querySelector('.subnav')

    if (window.scrollY > 100) {
        subnav.classList.add('scd')
        subnav.classList.remove('scu')
    }

    if (window.scrollY < 100) {
        subnav.classList.add('scu')
        subnav.classList.remove('scd')
    }
} )