
const table_report = document.getElementById('table');

function cargar_reportes(){
    
    axios.get('/listreports', {
            responseType: 'json'
        })
        .then(function(response) {
            const data = response.data
            let listre = '';
            for (let id_roles in data) {
                listre+= `<div class="table-responsive">
                <table class="table table-hover text-center">
                    <thead>
                        <tr class="success">
                            <th class="text-center">Tipo usuario</th>
                            <th class="text-center">N. Préstamos</th>
                            <th class="text-center">Porcentaje</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>${id_roles}</td>
                            <td>0</td>
                            <td>0%</td>
                        </tr>
                       
                    </tbody>
                    <tfoot>
                        <tr class="info">
                            <th class="text-center">Total</th>
                            <th class="text-center">0</th>
                            <th class="text-center">0%</th>
                        </tr>
                    </tfoot>
                </table>
                `;
            }
            table_report.innerHTML = listre
        })
        .catch(function(err) {
            console.log(err);
        })
        .then(function() {});
}