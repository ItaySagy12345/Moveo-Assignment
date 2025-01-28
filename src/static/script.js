const subtext = document.querySelector(".subtext");

const handleButtonClick = () => {
    if (subtext.innerHTML === 'hello' || subtext.innerHTML === "Hello") {
        subtext.innerHTML = 'World';
    } else {
        subtext.innerHTML = 'Hello';
    }
};
