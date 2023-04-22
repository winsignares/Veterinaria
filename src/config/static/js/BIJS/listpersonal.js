const morfismo = document.getElementById('poli');

function listaestudiantes() {
    axios.get('/conlistpersonal', {
            responseType: 'json'
        })
        .then(function(response) {
            const pico = response.datos
            let listper = '';
            for (let DUI in datos) {
                listper += `<div class="table-responsive">
                    <div class="div-table" style="margin:0 !important;">
                        <div class="div-table-row div-table-row-list">
                        <div class="div-table-cell" style="width: 6%;">#</div>
                        <div class="div-table-cell" style="width: 15%;">${DUI}</div>
                        <div class="div-table-cell" style="width: 15%;">${pico.Nombre}</div>
                        <div class="div-table-cell" style="width: 12%;">${pico.Telefono}</div>
                        <div class="div-table-cell" style="width: 15%;">${pico.Cargo}</div>
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
            morfismo.innerHTML = listper
        })
        .catch(function(err) {
            console.log(err);
        })
        .then(function() {});
}