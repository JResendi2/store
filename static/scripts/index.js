    const fileImg = document.querySelector("#file-img");
    const img = document.querySelector("#img");
    const name = document.querySelector("#name");
    const description = document.querySelector("#description");
    const price = document.querySelector("#price");
    const btnSave = document.querySelector("#btn-save");
    const btnAdd = document.querySelector("#btn-add");
    const btnUpdate = document.querySelector("#btn-update");
    const btnDelete = document.querySelector("#btn-delete");
    const containerNewProduct = document.querySelector("#new-product");
    const containerEditProduct = document.querySelector("#edit-product");
    const form = document.querySelector("#form");
    const toastHTML = document.querySelector("#toast");

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
                const toastBody = document.querySelector('#toast .toast-body p');
                toastBody.textContent = 'Producto eliminado';
                const toast = new bootstrap.Toast(toastHTML);
                toast.show();
                setTimeout(() => {
                    location.reload();
                }, 2000); 
            })
            .catch(error => console.error('Error:', error));
    }


    function getId(id) {
        containerNewProduct.classList.add("d-none");
        containerEditProduct.classList.remove("d-none");
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

    btnUpdate.addEventListener("click", (e) =>{
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
                const toastBody = document.querySelector('#toast .toast-body p');
                toastBody.textContent = 'Producto actualizado';
                const toast = new bootstrap.Toast(toastHTML);
                toast.show();
                console.log(data);
            })
            .catch(error => console.error('Error:', error));
        e.preventDefault();
    });

    btnAdd.addEventListener("click", (e) =>{
        containerNewProduct.classList.remove("d-none");
        containerEditProduct.classList.add("d-none");
    });

    btnSave.addEventListener("click", (e) =>{
        const form = document.querySelector("#form-new");
        const data = new FormData(form);
        fetch('create', {
            method: "POST",
            body: data
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                location.reload();
            })
            .catch(error => console.error('Error:', error));
        e.preventDefault();
    });