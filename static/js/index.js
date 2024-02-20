// popup function
let selector = document.getElementById('logo');
let popup = document.getElementById('popup');


selector.addEventListener('mouseenter', () =>{
    popup.style.display ='block';
})
popup.addEventListener('mouseleave', () =>{
    popup.style.display ='none';
})



// update details in profile
var displayLink = document.getElementById('link');
const hideContainer = document.getElementById('p-update');
const cancel = document.getElementById('cancel');

displayLink.addEventListener('click', ()=>{
    hideContainer.style.display='block';
})

// hide th e container
//cancel.addEventListener('click', ()=>{
//     hideContainer.style.display='none';
// })

// toggle the navbar

var togg = document.getElementById('toggle');
var sidebar = document.getElementById('container-fluid');
var main = document.getElementById('main');
var footer = document.getElementById('foot');
var menu = document.getElementById('menubar');

togg.addEventListener('click', ()=>{
  sidebar.classList.toggle("minimized");  
  main.classList.toggle("active");
  footer.classList.toggle('footer');
  menu.classList.toggle('menub');
})