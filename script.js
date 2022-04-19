function getAmounts() {
    fetch('/amounts.json').then(request => {
        return request.json()
    }).then(json => {
        console.log(json);
    });
}
getAmounts();
setInterval(getAmounts, 500);
