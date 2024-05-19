document.addEventListener('contextmenu', function (event) {
    var targetElement = event.target;
    // Verifica si el elemento clickeado es una imagen
    if (targetElement.tagName === 'IMG') {
        // Cancela el evento del botón derecho del mouse
        event.preventDefault();
    }
});