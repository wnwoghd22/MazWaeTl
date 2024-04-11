const links = document.querySelectorAll('a.post-item');

function clickLinkWithDelay(link, delay) {
    setTimeout(function() {
        link.click();
    }, delay);
}

links.forEach((link, index) => {
    const delay = (index + 1) * 15000;
    clickLinkWithDelay(link, delay);
});