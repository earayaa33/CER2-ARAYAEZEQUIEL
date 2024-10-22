

const residuoSeleccion = document.getElementById("residuo");
const subcategoriaSeleccion = document.getElementById("subcategoria");

/*Diccionario de categorias, utilizado posteriormente para cambiar las subopciones*/
const subcategorias = {
  plastico: ["Botellas", "Envases", "Bolsas"],
  papel: ["Periódicos", "Cartón", "Papel de oficina"],
  vidrio: ["Botellas", "Frascos", "Cristalería"],
  metales: ["Latas", "Cables", "Electrodomésticos pequeños"],
  electronicos: ["Teléfonos móviles", "Baterías", "Componentes de computadoras"]
};

/*Metodo que se activa cuando se selecciona algun tipo de residuo*/
residuoSeleccion.addEventListener("change", function() {
  const tipoResiduo = residuoSeleccion.value; //Guarda el valor actual seleccionado 
  subcategoriaSeleccion.innerHTML = '<option value="">Subcategoría</option>'; // Resetea las opciones de subcategoría

  if (tipoResiduo) { //Se ejecuta si se selecciono un tipo de residuo
    subcategorias[tipoResiduo].forEach(subcategoria => { //Busca el tipo de residuo en el diccionario
      const option = document.createElement("option");
      option.value = subcategoria.toLowerCase(); 
      option.text = subcategoria;
      subcategoriaSeleccion.appendChild(option);
      //Agregara cada subcategoria asignada a un tipo de residuo al menu desplegable de subcategorias
    });
  }
});

// Validación del formulario
document.getElementById("formReciclaje").addEventListener("submit", function(event) {
  event.preventDefault();

  //define constantes que tomaran los valores colocados en cada etiqueta
  const nombre = document.getElementById("nombre").value;
  const email = document.getElementById("email").value;
  const direccion = document.getElementById("direccion").value;
  const tipoResiduo = residuoSeleccion.value;
  const subcategoria = subcategoriaSeleccion.value;
  const cantidad = parseFloat(document.getElementById("cantidad").value);

  //Validación si existe algún campo vacio
  if (!nombre || !email || !direccion || !cantidad || !tipoResiduo || !subcategoria) {
    alert("Por favor, complete todos los campos obligatorios.");
    return;
  }
  
  //Validación si la cantidad ingresada es menor o igual a 0
  if (isNaN(cantidad) || cantidad <= 0) {
    alert("Por favor, ingrese una cantidad válida de residuos (mayor que 0).");
    return;
  }

  //Valida si el correo tiene un formato valido de nombreusuario + '@' + dominiomail + . + dominio de nivel superior de 2 o 3 caracteres.
  const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
  if (!emailPattern.test(email)) {
    alert("Por favor, ingrese un correo electrónico válido.");
    return;
  }

  // Obtener el elemento del toast
  const toastEl = document.getElementById('toastExito');
  const toast = new bootstrap.Toast(toastEl);

  // Mostrar el toast
  toast.show();

  
  //Resetea el formulario
  document.getElementById("formReciclaje").reset();

  subcategoriaSeleccion.innerHTML = '<option value="">Subcategoría</option>';
  
});