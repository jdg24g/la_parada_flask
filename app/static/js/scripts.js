window.addEventListener("DOMContentLoaded", (event) => {
  // Función para reducir el tamaño de la barra de navegación
  var minimiza = function () {
    const colapzar = document.body.querySelector("#mainNav");
    if (!colapzar) {
      return;
    }
    if (window.scrollY === 0) {
      colapzar.classList.remove("encoger");
    } else {
      colapzar.classList.add("encoger");
    }
  };

  // Reducir el tamaño de la barra de navegación
  minimiza();

  // Reducir el tamaño de la barra de navegación cuando se desplaza la página
  document.addEventListener("scroll", minimiza);

  // scrollspy
  const navegacion = document.body.querySelector("#mainNav");
  if (navegacion) {
    new bootstrap.ScrollSpy(document.body, {
      target: "#mainNav",
      rootMargin: "0px 0px -40%",
    });
  }

  // Colapsar la barra de navegación responsive cuando el botón de alternancia (toggler) está visible
  const hamburguesa = document.body.querySelector(".navbar-toggler");
  const responsiveNavItems = [].slice.call(
    document.querySelectorAll("#navbarResponsive .nav-link")
  );
  responsiveNavItems.map(function (responsiveNavItem) {
    responsiveNavItem.addEventListener("click", () => {
      if (window.getComputedStyle(hamburguesa).display !== "none") {
        hamburguesa.click();
      }
    });
  });

  //Ver dato ingresado en el input y comparar con el json y si ambos coincides crear un div
});
const OPCIONES = document.querySelector("#inputGroupSelect01");
const tablaHorario = document.getElementById("tablaHorario");
const MITABLA = document.getElementById("tabla");
const DESTINO = document.getElementById("destino");
const SALIDA = document.getElementById("salida");
const TBODY = document.getElementById("tbody");
const NUMERO = document.getElementById("numero");
const TARJETA = document.getElementById("tarjeta");
OPCIONES.addEventListener("change", (event) => {
  const selectedOption = event.target.value;
  if (selectedOption != "0") {
    console.log(selectedOption);

    busqueda(selectedOption);
    MITABLA.style.display = "table";
    TARJETA.style.display = "block";
  } else {
    console.log(selectedOption);

    console.log("No hay nada");
    MITABLA.style.display = "none";
    TARJETA.style.display = "none";
  }
});
function busqueda(selectedOption) {
  fetch("static/assets/data/horariosCel.json")
    .then((response) => response.json())
    .then((data) => {
      hours = data;
      console.log(hours[selectedOption]);
      TBODY.innerHTML = "";
      for (i of hours[selectedOption]) {
        if (i["Numero"].length == 8) {
          NUMERO.innerHTML = `<a href="tel:+595${i["Numero"]}">0${i["Numero"]}  <i class="fa-solid fa-phone-volume fa-shake"></i></a>`;
        } else {
          NUMERO.innerHTML = `<a id="ws" href="https://api.whatsapp.com/send?phone=595${i["Numero"]}">0${i["Numero"]} <i class="fa-brands fa-whatsapp fa-bounce" style="color: #008a49;"></i></a>`;
        }
        console.log(i["Destino"], i["HORA"]);
        TBODY.innerHTML += `<tr><td>${i["Destino"]}</td><td>${i["HORA"]}</td></tr>`;
      }
    })
    .catch((error) => {
      console.log("Error:", error);
    });
}
