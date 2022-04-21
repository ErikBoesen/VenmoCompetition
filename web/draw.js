function choose(amounts) {
    let ceiling = 0;
    for (let user in amounts) {
        ceiling += amounts[user];
    }
    let selection = Math.random() * ceiling;
    for (let user in amounts) {
        if (selection < amounts[user]) {
            return user;
        }
        selection -= amounts[user];
    }
}

function draw() {
    fetch('/user_amounts.json').then(request => {
        return request.json()
    }).then(amounts => {
        document.getElementById('winner').textContent = choose(amounts);
    });
}
document.getElementById('draw').onclick = draw;
