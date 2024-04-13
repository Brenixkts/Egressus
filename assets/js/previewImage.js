const avatarImage = document.querySelector('#logo-img')
const labelImg = document.querySelector('#label-img')

avatarImage.addEventListener('change', event => {

    const preview = document.querySelector('#preview-img')


    if(preview){
        preview.remove()
    }


    /* adicionando um new FileReader e configurando*/
    const reader = new FileReader

    reader.onload = function(event){

        const previewImage = document.createElement('img')
        previewImage.width = 160
        previewImage.height = 170
        previewImage.id = 'preview-img'
        previewImage.src = event.target.result
        
        /*inserindo a imagem na página após a label */
    
        labelImg.insertAdjacentElement('afterend', previewImage)

    }


        reader.readAsDataURL(avatarImage.files[0])

})