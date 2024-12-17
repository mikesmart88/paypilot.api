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


// sidebar program

let is_open = false;
function side_bar() {
    if (is_open == false) {
        document.getElementById('side_bar').style.top = '5%';
        document.getElementById('menu_box').innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x" viewBox="0 0 16 16">
  <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708"/>
</svg>`;
is_open = true;
    } 
else{
        document.getElementById('side_bar').style.top = '-600px';
        document.getElementById('menu_box').innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-list" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5"/>
                  </svg>`;
                  is_open = false;
    }

}