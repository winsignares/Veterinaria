function Guardarlibros() {
    const titulobook = document.getElementById('titulolibro');
    const id_autorbook = document.getElementById('autorlibro');
    const paisbook = document.getElementById('paislibro');
    const id_Categoriabook = document.getElementById('categorialibro');
    const id_proveedorbook = document.getElementById('proveedorlibro');
    const ano_publicadobook = document.getElementById('yearlibro');
    const editorialbook = document.getElementById('editoriallibro');
    const ubicacionbook = document.getElementById('ubicacionlibro');
    const estimadobook = document.getElementById('estimadolibro');
    const cargobook = document.getElementById('cargobook');
    const estadobook = document.getElementById('estadolibro');

    /*alert(titulobook.value);
    alert(id_autorbook.value);
    alert(paisbook.value);
    alert(id_Categoriabook.value);
    alert(id_proveedorbook.value);
    alert(ano_publicadobook.value);
    alert(editorialbook.value);
    alert(ubicacionbook.value);
    alert(estimadobook.value);
    alert(cargobook.value);
    alert(estadobook.value);*/
    //passadmin.value === passadmin2.value ? alert(`Estos son los datos del administrador ${nameadmin.value} ${emailadmin.value}${usernameadmin.value} ${passadmin.value}`): alert('los campos son diferentes');
    axios.post('guardarbook', {
        titulo: titulobook.value,
        id_autor: id_autorbook.value,
        pais: paisbook.value,
        id_Categoria: id_Categoriabook.value,
        id_proveedor: id_proveedorbook.value,
        ano_publicado: ano_publicadobook.value,
        editorial: editorialbook.value,
        ubicacion: ubicacionbook.value,
        estimado: estimadobook.value,
        cargo: cargobook.value,
        estado: estadobook.value
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

window.onload = function () {
    mostaratorbook();
}

const selautorlibro = document.getElementById('autorlibro');
//const axios = require('axios');

selautorlibro.addEventListener('change', function () {
    // Hacer una petición para un usuario con ID especifico
    axios.get('/api/autores')
        .then(function (response) {
            // manejar respuesta exitosa
            console.log(response.data);
            const data = response.data
            for (items in data) {
                alert(data[items].nombre)
                const opcion = document.createElement('option');
                opcion.value = data[items].id;
                opcion.text = data[items].nombre;
                selautorlibro.appendChild(selautorlibro);            
            }
        })
        .catch(function (error) {
            // manejar error
            console.log(error);
        })
        .finally(function () {
            // siempre sera executado
            console.log("Ejcucion Finalizada");
        });
}, false);



function mostaratorbook() {
    const selectautor = document.getElementById("autorlibro");
        axios.get('/libros')
        .then(function (response) {
            alert(response.data)
          const options = response.data;
          const select = document.getElementById('autorlibro');
          options.map(function(option) {
            const el = document.createElement("option");
            el.text = option[1];
            el.value = option[0];
            select.add(el);
          });
        })
        .catch(function (error) {
          console.log(error);
        });
}

function eliminar() {
    const div = document.getElementById("hola");
    div.parentNode.removeChild(div);
}