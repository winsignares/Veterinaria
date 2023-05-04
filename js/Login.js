const loginsec = document.querySelector('.login-section')
const loginlink = document.querySelector('.login-link')
const registerlink = document.querySelector('.register-link')
registerlink.addEventListener('click', () => {
    loginsec.classList.add('active')
})
loginlink.addEventListener('click', () => {
        loginsec.classList.remove('active')
    }) /

    function login() {
        var user, pass

        user = document.getElementById("usuario").value;
        pass = document.getElementById("contraseña").value;

        if (user == "antonio" && pass == 1234) {
            alert("INICIANDO")

        } else {
            alert("Datos incorrectos")
        }




    }