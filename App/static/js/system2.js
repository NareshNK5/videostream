document.addEventListener('DOMContentLoaded', function() {
    const ws = new WebSocket('ws://' + window.location.host + '/ws/control/');

    ws.onmessage = function(e) {
        const data = JSON.parse(e.data);
        const command = data.command;

        if (command === 'video') {
            playVideo();
        } else if (command === 'audio') {
            playAudio();
        } else if (command === 'image') {
            showImage();
        }
    };

    function playVideo() {
        const video = document.getElementById('video');
        if (video) {
            video.style.display = 'block';
            video.play();
        }
    }

    function playAudio() {
        const audio = document.getElementById('audio');
        if (audio) {
            audio.style.display = 'block';
            audio.play();
        }
    }

    function showImage() {
        // Example: Assuming there is an image element with id 'image'
        const image = document.getElementById('image');
        if (image) {
            image.style.display = 'block';
        }
    }
});
