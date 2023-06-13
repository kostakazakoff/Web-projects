function handleImgUpload() {
    const uploadField = document.getElementById('upload_file');
    uploadField.innerHTML = '<input type="file" name="photo" accept="image/*" id="id_photo"></input>';

    const deleteField = document.getElementById('delete_file');
    deleteField.innerHTML = '<label for="photo-clear_id">Delete photo<input type="checkbox" name="photo-clear" id="photo-clear_id"></label>'

    const imgInput = document.getElementById('id_photo');
    const imgPreview = document.getElementById('img_preview');

    imgInput.addEventListener('change', (event) => {
        imgPreview.classList = ['photo'];
        const imgObj = event.target.files[0];
        imgPreview.src = URL.createObjectURL(imgObj);
    });
}

handleImgUpload()
