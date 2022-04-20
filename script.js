function getAmounts() {
    fetch('/amounts.json').then(request => {
        return request.json()
    }).then(amounts => {
        for (let artist in amounts) {
            document.getElementById(artist).textContent = '$' + amounts[artist].toFixed(2);
        }
    });
}
getAmounts();
setInterval(getAmounts, 2000);
