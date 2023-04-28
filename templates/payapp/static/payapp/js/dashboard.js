const closeBtn = document.getElementById('close');
const sendBtn = document.getElementById('send');

// toggle
closeBtn.addEventListener('click', () => {
    console.log('clicked');
    document.querySelector('.popup').classList.toggle('hidden');
    document.querySelector('.popup-card').classList.toggle('hidden');
});

// send
sendBtn.addEventListener('click', () => {
    console.log('clicked');
    document.querySelector('.popup').classList.toggle('hidden');
    document.querySelector('.popup-card').classList.toggle('hidden');
})