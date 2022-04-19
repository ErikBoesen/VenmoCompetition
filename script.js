function getAmounts() {
    fetch('/amounts.json').then(request => {
        return request.json()
    }).then(json => {
        console.log(json);
    });
}
