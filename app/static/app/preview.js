document.addEventListener('DOMContentLoaded', e => {
    for (const fileInput of document.querySelectorAll('input.preview-marker')) {
        const img = document.getElementById(fileInput.dataset.target);
        if (img) {
            fileInput.addEventListener('change', e => {
                img.src = window.URL.createObjectURL(e.target.files[0]);
            });
            const initialURL = fileInput.dataset.initial;
            if (initialURL) {
                img.src = initialURL;
            }
        }
    }
});
