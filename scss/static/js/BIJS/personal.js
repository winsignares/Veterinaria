function Guardarperonal() {
    const NumDUI = document.getElementById('Numero_de_DUIAdmin');
    const NomAdmin = document.getElementById('NombresAdmin');
    const ApellAdmin = document.getElementById('ApellidosAdmin');
    const TelAdmin = document.getElementById('TelefonoAdmin');
    const CargAdmin = document.getElementById('CargoAdmin');
    const NomUsuario = document.getElementById('NomUsuario');
    const ContraseñaAdmin = document.getElementById('ContraseñaAdmin');
    const ContraseñaAdmin2 = document.getElementById('ContraseñaAdmin2');


    axios.post('guardarperso', {
        fullname: NumDUI.value,
        NombresAdmin: NomAdmin.value,
        ApellidosAdmin: ApellAdmin.value,
        TelefonoAdmin: TelAdmin.value,
        CargoAdmin: CargAdmin.value,
        NombreUsuario: NomUsuario.value,
        ContraseñaAdmin: ContraseñaAdmin.value,
        ContraseñaAdmin2: ContraseñaAdmin2.value
      

    }, {
        headers: {
        'Content-Type': 'multipart/form-data'

        }
    }
    ).then((res) => {
        console.log(res.data)
    })
    .catch((error) => {
        console.error(error)
    })
}
function DatoSeguro() {
    Swal.fire({
        title: 'Deseas Guardar este dato',
        text: 'Recuerda que este dato será almacenado',
        confirmButtonText: 'confirmar',
        showCancelButton: true,
        icon: 'warning'

    })
};

