"use strict"

// intersection observer program

function _(c) { return document.getElementById(c); }

var _sect = _('min_sect1');



const observer = new IntersectionObserver(
    callbackfucntion,
    option,
)

function callbackfucntion(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            if (entry.target.id === 'min_sect1') {
                entry.target.classList.add('trim')
            }
        }
    });
}

var option = {
    rootMargin: "0px",
    threshold: 1,
}

observer.observe(_sect)

