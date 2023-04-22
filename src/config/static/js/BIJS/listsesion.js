const divcategory = document.getElementById('llenar')
function listsection(){
    alert('fdsfds')
  Axios.get('/listasection', {
    responseType: 'json'
})
.then(function(response) {
    const datos = response.data
    let section = '';
    for (let id in datos) {
        section += `<div class="div-table-row">
      <div class="div-table-cell">${id}</div>
      <div class="div-table-cell">${datos.nombre}</div>
      <div class="div-table-cell">${datos.elimar}</div>
      <div class="div-table-cell">  
          <button class="btn btn-success">eliminar<i class="zmdi zmdi-refresh"></i></button>
      </div>
      
  </div>`;
    }
    divcategory.innerHTML = category
})
.catch(function(err) {
    console.log(err);
})
.then(function() {});

}