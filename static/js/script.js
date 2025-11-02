// 🎵 Play/Pause background music
function toggleMusic() {
    let audio = document.getElementById("bg-music");
    let btn = document.getElementById("music-btn");

    if (audio.paused) {
        audio.play();
        btn.innerText = "⏸ Pause Music";
    } else {
        audio.pause();
        btn.innerText = "▶ Play Music";
    }
}

// 🌟 Simple button click animation
function buttonClickEffect() {
    let btn = document.getElementById("music-btn");
    btn.style.transform = "scale(1.2)";
    setTimeout(() => {
        btn.style.transform = "scale(1)";
    }, 200);
}

// 💫 Floating message effect
function showMessage() {
    let msg = document.createElement("div");
    msg.innerText = "🎶 Music is life!";
    msg.style.position = "fixed";
    msg.style.bottom = "20px";
    msg.style.right = "20px";
    msg.style.padding = "10px 20px";
    msg.style.background = "rgba(0,0,0,0.7)";
    msg.style.color = "white";
    msg.style.borderRadius = "10px";
    msg.style.fontSize = "1rem";
    msg.style.zIndex = "1000";

    document.body.appendChild(msg);

    setTimeout(() => {
        msg.remove();
    }, 2000);
}
