document.addEventListener('DOMContentLoaded', function () {
    // Agregar evento dragstart a todas las imágenes
    var images = document.querySelectorAll('img');
    images.forEach(function (image) {
        // Evitar el evento dragstart
        image.addEventListener('dragstart', function (event) {
            event.preventDefault(); // Evitar el comportamiento predeterminado de arrastrar
        });

        // Evitar el menú contextual (clic derecho)
        image.addEventListener('contextmenu', function (event) {
            event.preventDefault(); // Evitar el menú contextual
        });
    });
});