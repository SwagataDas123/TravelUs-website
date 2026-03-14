let searchBtn=document.querySelector('#search-btn');
let searchBar=document.querySelector('.search-bar-container');
let formBtn=document.querySelector('#login-btn');
let loginForm=document.querySelector('.login-form-container');
let formClose=document.querySelector('#form-close');
let menu=document.querySelector('#menu-bar');
let navbar=document.querySelector('.navbar');
let videoBtn=document.querySelectorAll('.vid-btn');

// NEW: register form elements
//let registerBtn = document.querySelector('#register-btn');
let registerForm=document.querySelector('#register-form');
let registerClose=document.querySelector('#register-close');
let showRegister=document.querySelector('#show-register');
let showLogin=document.querySelector('#show-login');

window.onscroll = () =>{
searchBtn.classList.remove('fa-times');
searchBar.classList.remove('active');
menu.classList.remove('fa-times');
navbar.classList.remove('active');
loginForm.classList.remove('active');
registerForm.classList.remove('active');//new
}



menu.addEventListener('click',() =>{
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
    });

searchBtn.addEventListener('click',() =>{
searchBtn.classList.toggle('fa-times');
searchBar.classList.toggle('active');
});

formBtn.addEventListener('click',() =>{
    loginForm.classList.add('active');
    });

/*formBtn.addEventListener('click',(e)=>{
    e.preventDefault();
    window.open("https://travel-pal--sdas23366.replit.app", "_blank");
});*/

formClose.addEventListener('click',() =>{
    loginForm.classList.remove('active');
    });
// Open register popup
/*registerBtn.addEventListener('click', (e) => {
    e.preventDefault(); // stop page reload
    loginForm.classList.remove('active'); // hide login if open
    registerForm.classList.add('active'); // show register
});
*/
// Close register popup
registerClose.addEventListener('click', () => {
    registerForm.classList.remove('active');
});
  
// Show register
showRegister.addEventListener('click',(e)=>{
    e.preventDefault();
    loginForm.classList.remove("active");
    registerForm.classList.add("active");
});

// Show login
showLogin.addEventListener('click',(e)=>{
    e.preventDefault();
    registerForm.classList.remove("active");
    loginForm.classList.add("active");
});

// Close register
registerClose.addEventListener('click',()=>{
    registerForm.classList.remove("active");
});

    videoBtn.forEach(btn =>{
btn.addEventListener('click',()=>{
document.querySelector('.controls .active').classList.remove('active');
btn.classList.add('active');
let src=btn.getAttribute('data-src');
document.querySelector('#video-slider').src=src;
});
});
var swiper = new Swiper(".review-slider", {
    spaceBetween:20,
    loop:true,
    autoplay:{
        delay:2500,
        disableOnInteraction:false,
    },
    breakpoints:{
        640:{
            slidesPerView:1,
        },
        768:{
            slidesPerView:2,
        },
        1024:{
            slidesPerView:3,
        },
    },
});

var swiper = new Swiper(".brand-slider", {
    spaceBetween:40,
    loop:true,
    autoplay:{
        delay:2500,
        disableOnInteraction:false,
    },
    breakpoints:{
        450:{
            slidesPerView:2,
        },
        768:{
            slidesPerView:3,
        },
        991:{
            slidesPerView:4,
        },
        1200:{
            slidesPerView:5,
        },
    },
});

/*const chatbotContainer = document.getElementById('chatbot-container');
    const chatbotMessages = document.getElementById('chatbot-messages');
    const chatbotInput = document.getElementById('chatbot-input');
    const sendMessageButton = document.getElementById('send-message');
    const closeChatbotButton = document.getElementById('close-chatbot');*/

    // Show the chatbot
   /* document.getElementById('login-btn').addEventListener('click', () => {
        chatbotContainer.style.display = 'flex';
    });*/

    //chatbot opens in new tab _blank
   /* document.getElementById('login-btn').addEventListener('click', () => {
    window.open("https://travel-pal--sdas23366.replit.app", "_blank");
});*/

    // Close the chatbot
    /*closeChatbotButton.addEventListener('click', () => {
        chatbotContainer.style.display = 'none';
    });

    // Send a message
    sendMessageButton.addEventListener('click', () => {
        const userMessage = chatbotInput.value.trim();
        if (userMessage) {
            addMessage('You', userMessage);
            chatbotInput.value = '';
            setTimeout(() => {
                addMessage('Bot', 'Thank you for reaching out! How can I help you today?');
            }, 1000);
        }
    });
    */

    