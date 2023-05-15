const buscador = document.getElementById('buscali');

function buscarlibro() {
    axios.get('/libros',  {
            responseType: 'json'
        })
        .then(function(response) {
            const pico = response.datos
            let buslibro = '';
            for (let id in datos) {
                listper += `<div class="table-responsive">
                    <div class="div-table" style="margin:0 !important;">
                        <div class="div-table-row div-table-row-list">
                        <div class="div-table-cell" style="width: 6%;">#</div>
                        <div class="div-table-cell" style="width: 15%;">${id}</div>
                        <div class="div-table-cell" style="width: 15%;">${pico.titulo}</div>
                        <div class="div-table-cell" style="width: 15%;">${pico.id_autor}</div>
                        <div class="div-table-cell" style="width: 15%;">${pico.id_pais}</div>
                        <div class="div-table-cell" style="width: 15%;">${pico.Categoria}</div>
                        <div class="div-table-cell" style="width: 15%;">${pico.id_proveedor}</div>
                        <div class="div-table-cell" style="width: 15%;">${pico.ano_publicado}</div>
                        <div class="div-table-cell" style="width: 15%;">${pico.editorial}</div>
                        <div class="div-table-cell" style="width: 15%;">${pico.ubicacion}</div>
                        <div class="div-table-cell" style="width: 15%;">${pico.estimado}</div>
                        <div class="div-table-cell" style="width: 15%;">${pico.cargo}</div>
                        <div class="div-table-cell" style="width: 15%;">${pico.estado}</div>
                        <div class="div-table-cell" style="width: 9%;">
                                <button class="btn btn-success"><i class="zmdi zmdi-refresh"></i></button>
                            </div>
                            <div class="div-table-cell" style="width: 9%;">
                                <button class="btn btn-danger"><i class="zmdi zmdi-delete"></i></button>
                            </div>
                        </div>
                    </div>
                </div>`;
            }
            buscador.innerHTML = buslibro
        })
        .catch(function(err) {
            console.log(err);
        })
        .then(function() {});
}