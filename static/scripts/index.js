    const fileImg = document.querySelector("#file-img");
    const img = document.querySelector("#img");
    const name = document.querySelector("#name");
    const description = document.querySelector("#description");
    const price = document.querySelector("#price");
    const btnSave = document.querySelector("#btn-save");
    const btnDelete = document.querySelector("#btn-delete");
    const form = document.querySelector("#form");
    let product_id;

    function deleteProduct(e){
        formDelete = e.parentNode;
        const data = new FormData(formDelete);
        const actionUrl = formDelete.action;
        fetch(actionUrl, {
            method: "POST",
            body: data
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                location.reload();
            })
            .catch(error => console.error('Error:', error));
    }


    function getId(id) {
        fetch('view-data/'+id)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                name.value = data.name;
                description.value = data.description;
                img.src = data.img;
                price.value = data.price;

                product_id = id;
            })
            .catch(error => console.error('Error:', error));
    }

    fileImg.addEventListener('change', function () {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                img.src = e.target.result;
            }
            reader.readAsDataURL(file);
        }
    });

    btnSave.addEventListener("click", (e) =>{
        if(name.value === "" || description.value === "" || price.value === ""){
            return;
        }
        const data = new FormData(form);
        fetch('update/'+product_id, {
            method: "POST",
            body: data
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);
            })
            .catch(error => console.error('Error:', error));
        e.preventDefault();
    });