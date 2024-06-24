document.addEventListener("DOMContentLoaded", function () {
    const btnAddProduct = document.querySelector("#btn-add-product");
    
    let btnLoginClient = null;
    let btnRegister = null;
    let btnSaveClient = null;
    const modalRegisterHtml = document.querySelector("#modal-register");
    const modalRegister = new bootstrap.Modal(modalRegisterHtml);

    const modalBody = modalRegisterHtml.querySelector(".modal-body");

    btnAddProduct.addEventListener("click", (e) => {
        e.preventDefault();
        fetch('/login/loggedin_user/')
            .then(response => response.json())
            .then(data => {
                if(data.authenticated){
                    console.log("Tu compra ha sido agregada a tu carrito :)");
                } else {
                    const token = modalRegisterHtml.querySelector('input[name="csrfmiddlewaretoken"]');
                    modalBody.innerHTML = data.body;
                    const form = modalBody.querySelector("form");
                    form.appendChild(token);
                    btnRegister = modalBody.querySelector("#btn-register");
                    btnRegister.addEventListener("click", (e) => openModalRegister(e));
                    btnLoginClient = modalBody.querySelector("#btn-login-client");
                    btnLoginClient.addEventListener("click", (e) => loginClient(e));
                    modalRegister.show();
                }
            })
            .catch(error => console.error('Error:', error));
    })

    function loginClient(e){
        e.preventDefault();
        const form = new FormData(modalBody.querySelector("#form-register"));
        fetch('/login/login_in_client/', {
            method: "POST",
            body: form
        })
            .then(response => response.json())
            .then(data => {
                if(data.session === true){
                    modalRegister.hide();
                    console.log("Tu compra ha sido agregada a tu carrito :)");
                } else {
                    const token = modalRegisterHtml.querySelector('input[name="csrfmiddlewaretoken"]');
                    modalBody.innerHTML = data.body;
                    const form = modalBody.querySelector("form");
                    
                    btnLoginClient = modalBody.querySelector("#btn-login-client");
                    btnLoginClient.addEventListener("click", (e) => loginClient(e));
                    btnRegister = modalBody.querySelector("#btn-register");
                    btnRegister.addEventListener("click", (e) => openModalRegister(e));
                    form.appendChild(token);
                }
            })
            .catch(error => console.error('Error:', error));
    }


    function openModalRegister(e){
        e.preventDefault();
        fetch('/login/login_up_client/', {
            method: "GET",
        })
            .then(response => response.json())
            .then(data => {
                const token = modalRegisterHtml.querySelector('input[name="csrfmiddlewaretoken"]');
                modalBody.innerHTML = data.body;
                const form = modalBody.querySelector("form");
                form.appendChild(token);
                btnSaveClient = modalBody.querySelector("#btn-save-client");
                btnSaveClient.addEventListener("click", (e) => saveClient(e));
            })
            .catch(error => console.error('Error:', error));
    }

    function saveClient(e){
        e.preventDefault();
        const form = new FormData(modalBody.querySelector("#form-register"));
        fetch('/login/login_up_client/', {
            method: "POST",
            body: form
        })
            .then(response => response.json())
            .then(data => {
                const token = modalRegisterHtml.querySelector('input[name="csrfmiddlewaretoken"]');
                modalBody.innerHTML = data.body;
                const form = modalBody.querySelector("form");
                form.appendChild(token);
            })
            .catch(error => console.error('Error:', error));
    }

})