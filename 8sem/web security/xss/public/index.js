const XSS_SYMBOLS = [/&/g, /</g, />/g, /"/g, /'/g];

const sendReviewFx = async (data) => {
    fetch(`/file?title=${data.title}&text=${data.text}`, {
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
        method: "POST"
    })
}

const getReviewsFx = async () => {
    const get = await fetch('/file', {
        headers: {
            "Content-Type": "application/json",
        },
        method: "GET"
    });
    return get.text();
};

const checkText = (str) => {
    for (let i = 0; i < XSS_SYMBOLS.length; i++) {
        const symbol = XSS_SYMBOLS[i];
        if (symbol.test(str)) {
            return false
        };
    }
    return true;
}

const sendReview = async () => {
    const title = document.getElementById('title');
    const text = document.getElementById('text');
    if (!checkText(title.value) || !checkText(text.value)) {
        alert("Небозопасный ввод");
    }
    const obj = {
        title: title.value,
        text: text.value
    };
    sendReviewFx(obj);
};

const getReviews = async () => {
    const text = await getReviewsFx();
    const reviews = document.getElementById('reviews');
    reviews.innerHTML = text;
}

getReviews();
