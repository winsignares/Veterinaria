//----------------------------------------------------------------
function addSection() {
    const OpYear = document.getElementById('getOptionYear').value;
    const OpEspecialidad = document.getElementById('getOptionEspecialidad').value;
    const OpSeccion = document.getElementById('getOptionSeccion').value;

    axios.post('guardarsection', {
            year: OpYear,
            especialidad: OpEspecialidad,
            seccion: OpSeccion


        }, {
            headers: {
                'Content-Type': 'multipart/form-data'

            }
        }).then((res) => {
            console.log(res.data)
        })
        .catch((error) => {
            console.error(error)
        })
}