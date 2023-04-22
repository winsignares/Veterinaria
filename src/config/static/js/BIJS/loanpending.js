/*function eliminar() {
    /*    const div = document.getElementById("hola");
        div.parentNode.removeChild(div);
alert("algo")
}*/

function Listo() {
    const Toast = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 3000,
        timerProgressBar: true,
        didOpen: (toast) => {
            toast.addEventListener('mouseenter', Swal.stopTimer)
            toast.addEventListener('mouseleave', Swal.resumeTimer)
        }
    })

    Toast.fire({
        icon: 'success',
        title: 'Recibido con Exito'
    })
    tblestadosolicitud.ajax.reload(null, flase)
}

function fmodal() {
    // Obtén el modal y el botón de cerrar
    const openModal = document.querySelector('.modal_button')
    const modal = document.querySelector('.modal1');
    const close_Modal = document.querySelector('.close_Modal');

    // Añade un evento click al botón de cerrar para cerrar el modal
    openModal.addEventListener('click', () => {
        modal.classList.add('modal-show');
    })

    // Añade un evento click a cualquier parte del modal para cerrarlo también
    close_Modal.addEventListener('click', (e) => {
        modal.classList.remove('modal-show')
    })
}