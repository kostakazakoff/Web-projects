function preview() {
    const imgInput = document.getElementById('id_photo');
    const imgPreview = document.getElementById('img_preview');
    imgInput.addEventListener('change', (event) => {
        imgPreview.classList = ['photo'];
        const imgObj = event.target.files[0];
        imgPreview.src = URL.createObjectURL(imgObj);
    });
}

preview()