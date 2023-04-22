function GuardarInstructor() {
    const ccinstructor = document.getElementById('idinstructor');
    const nameinstructor = document.getElementById('nombreinstructor');
    const apeinstructor = document.getElementById('apellidoinstructor');
    const full = nameinstructor + apeinstructor;
    const telinstructor = document.getElementById('celinstructor');
    const espeinstructor = document.getElementById('espeinstruc');
    const usernameintruc = document.getElementById('usernameinstructor');
    const turnoinstruc = document.getElementById('jornadainstruc');    
    const secinstruc = document.getElementById('seccioninstruc');
    const passintruc = document.getElementById('passinstructor');
    const passinstruc = document.getElementById('passinstructor2');

    axios.post('save_Users', {
        full_name: full.value,
        Email: usernameintruc.value,
        Telefono: telinstructor.value,
        Especialidad: espeinstructor.value,
        Jornada: turnoinstruc.value,
        password: passintruc.value,
        Cedula: ccinstructor.value                
       
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