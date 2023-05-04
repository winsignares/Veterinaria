
const formulario = document.querySelector('#formulario');
const mensajeInput = document.querySelector('#mensaje');
const mensajesContainer = document.querySelector('#mensajes');

formulario.addEventListener('submit', function(evento) {
  evento.preventDefault();
  const mensaje = mensajeInput.value;
  mensajeInput.value = '';
  const mensajeElemento = document.createElement('div');
  mensajeElemento.innerText = mensaje;
  mensajesContainer.appendChild(mensajeElemento);
});
