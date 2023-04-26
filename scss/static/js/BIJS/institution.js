//este es el js de istitution
function Guardarinstitution() {
    const codigoinfra = document.getElementById('codigoinfra');
    const nombreinsti = document.getElementById('nombreinsti');
    const distrito = document.getElementById('Distrito');
    const telefono = document.getElementById('telefono');
    const año = document.getElementById('año');

    //passadmin.value === passadmin2.value ? alert(`Estos son los datos del administrador ${nameadmin.value} ${emailadmin.value}${usernameadmin.value} ${passadmin.value}`): alert('los campos son diferentes');
    axios.post('guardarinstitution', {
        //en el fullname va el dato de la base de datos
        fullname: fullname.value,
        nombre: nombreinsti.value,
        distrito: distrito.value,
        telefono: telefono.value,
        año: año.value
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