    
const botonCarrito = document.querySelector('.container-cart-icon');
const productosCarrito = document.querySelector(
	'.container-cart-products'
);

botonCarrito.addEventListener('click', () => {
	productosCarrito.classList.toggle('hidden-cart');
});

/* NUEVOOOO */
const carritoInfo = document.querySelector('.cart-product');
const filasCarrito = document.querySelector('.row-product');
const productosLista = document.querySelector('.container-items');
let productos = [];
const valorTotal = document.querySelector('.total-pagar');
const contadorProductos = document.querySelector('#contador-productos');
const carritoVacio = document.querySelector('.cart-empty');
const carritoTotal = document.querySelector('.cart-total');


//VERIFICAMOS QUE EXISTA PRODUCLIST
if (productosLista) {
    productosLista.addEventListener('click', e => {
      if (e.target.classList.contains('btn-add-cart')) {
        const product = e.target.parentElement;
        const infoProducto = {
          quantity: 1,
          title: product.querySelector('h2').textContent,
          price: product.querySelector('p').textContent,
        };
        const exits = productos.some(product => product.title === infoProducto.title);
        if (exits) {
          const products = productos.map(product => {
            if (product.title === infoProducto.title) {
              product.quantity++;
              return product;
            } else {
              return product;
            }
          });
          productos = [...products];
        } else {
            productos = [...productos, infoProducto];
        }
        showHTML();
      }
    });
  }

filasCarrito.addEventListener('click', e => {
    if (e.target.classList.contains('icon-close')) {
      const product = e.target.parentElement;
      const title = product.querySelector('p').textContent;
      productos = productos.filter(
      product => product.title !== title
        );
      console.log(productos);
      showHTML();
    }
});

const showHTML = () => {
  if (!productos.length) {
      carritoVacio.classList.remove('hidden');
      filasCarrito.classList.add('hidden');
      carritoTotal.classList.add('hidden');
    } else {
      carritoVacio.classList.add('hidden');
      filasCarrito.classList.remove('hidden');
      carritoTotal.classList.remove('hidden');
    }
filasCarrito.innerHTML = '';
  let total = 0;
  let totalOfProducts = 0;

    productos.forEach(product => {
      const containerProduct = document.createElement('div');
      containerProduct.classList.add('cart-product');
      containerProduct.innerHTML = `
          <div class="info-cart-product">
              <span class="cantidad-producto-carrito">${product.quantity}</span>
              <p class="titulo-producto-carrito">${product.title}</p>
              <span class="precio-producto-carrito">${product.price}</span>
          </div>
          <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="icon-close"
          >
              <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M6 18L18 6M6 6l12 12"
              />
          </svg>
      `;

      filasCarrito.append(containerProduct);

      total = total + parseInt(product.quantity * product.price.slice(1));
      totalOfProducts = totalOfProducts + product.quantity;
    });
      valorTotal.innerText = `$${total}`;
      contadorProductos.innerText = totalOfProducts;
};




//VALIDAR CAMPOS FORMULARIO REGISTRO
$(document).ready(function() {
  $('#form').on('submit', function(event) {
    var emailFormulario = $('#email').val();
    var nombreFormulario = $('#nombre').val().trim();
    var apellidoFormulario = $('#apellido').val().trim();
    var telefonoFormulario = $('#telefono').val().replace(/\s+/g, '').replace(/-/g, '');
    var contrasenaFormulario = $('#contrasena').val();
    var errorMessages = [];
    if (!emailFormulario || !/\S+@\S+\.\S+/.test(emailFormulario)) {
      errorMessages.push('Ingrese un correo electrónico válido.');
    }
    if (!/^[A-Za-zÁÉÍÓÚáéíóúÑñ\s']+$/.test(nombreFormulario)) {
      errorMessages.push('Ingrese un nombre válido (solo letras).');
    }
    if (!/^[A-Za-zÁÉÍÓÚáéíóúÑñ\s']+$/.test(apellidoFormulario)) {
      errorMessages.push('Ingrese un apellido válido (solo letras).');
    }
    if (!/^\d{9}$/.test(telefonoFormulario)) {
      errorMessages.push('Ingrese un número de teléfono válido (9 números).');
    }

    var contrasena = contrasenaFormulario;
    if (contrasena.length > 50) {
      errorMessages.push('La contraseña no puede tener más de 50 caracteres.');
    }
    var contieneMayuscula = /[A-Z]/.test(contrasena);
    var contieneMinuscula = /[a-z]/.test(contrasena);
    var contieneNumero = /\d/.test(contrasena);
    if (!contieneMayuscula || !contieneMinuscula || !contieneNumero) {
      errorMessages.push('La contraseña debe contener al menos una letra mayúscula, una letra minúscula y un número.');
    }

    if (errorMessages.length > 0) {
      event.preventDefault();

      var errorMessageContainer = $('#error-messages');
      errorMessageContainer.html('');
      $.each(errorMessages, function(index, message) {
        errorMessageContainer.append('<div>' + message + '</div>');
      });
    } else {
      alert('Registro exitoso.');
      $('#overlay').hide();
    }
  });
});

//CAMBIAR MODO OSCURO
document.getElementById('darkModeSwitch').addEventListener('change', function() {
    document.body.classList.toggle('dark-mode');
    document.getElementById('barra-verde').classList.toggle('dark-mode');
  });

  
//CANCELAR FORMULARIO
function cancelar() {

    alert('Operación cancelada.');
    var overlay = document.getElementById('overlay');
    overlay.style.display = 'none';
}
//BOTON REGISTRO FORMULARIO
document.getElementById('botonRegistro').addEventListener('click', function() {
    document.getElementById('overlay').style.display = 'flex';
});
//CERRAR FORMULARIO
document.getElementById('closeFormButton').addEventListener('click', function() {
    document.getElementById('overlay').style.display = 'none';
});


document.addEventListener('DOMContentLoaded', function() {
  var darkModeSwitch = document.getElementById('darkModeSwitch');

  darkModeSwitch.addEventListener('change', function() {
    if(this.checked) {
      enableDarkMode();
    } else {
      disableDarkMode();
    }
  });
  if(isDarkModeEnabled()) {
    darkModeSwitch.checked = true;
    enableDarkMode();
  } else {
    darkModeSwitch.checked = false;
    disableDarkMode();
  }
});

function enableDarkMode() {
  document.body.classList.add('dark-mode');
}

function disableDarkMode() {
  document.body.classList.remove('dark-mode');
}

function isDarkModeEnabled() {

  return false;
}

