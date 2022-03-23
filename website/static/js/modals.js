const modalBody = document.getElementById('modal-body')
const modal = document.getElementById("myModal");
const sc = document.getElementById('sc')
const buttonTop = document.getElementById('ScrollBtn')

$.ajax({

    type: "GET",

    url: "/data-json",

    success: function () {

        const product = [...document.getElementsByClassName('trigger')]

        product.forEach(item => item.addEventListener('click', e => {

            const name = e.target.getAttribute('data-name')
            const pic = e.target.getAttribute('src')
            const desc = e.target.getAttribute('data-desc')
            const price = e.target.getAttribute('data-price')
            const unite = e.target.getAttribute('data-unite')
            const dispo = e.target.getAttribute('data-dispo')
            const static = e.target.getAttribute('data-static')

            console.log(e.target)

            if (dispo == 'True'){

                modalBody.innerHTML = `<img src=${pic} alt="Image du produit">`

            }else{

                modalBody.innerHTML = `

                        <img class="over" src=${pic} alt="Image du produit">        

                `

            }

          
            modalBody.innerHTML += `

                <h2>${name}</h2>

                <hr>

                <h3><span>${desc}</span></h3>

                <hr>

                <p>${price}€ / ${unite}</p>

                <div class="modal-bottom">

                    <img class="modal-picture" id="ckeck" src="${static}img/check.svg" alt="Icon indiquant que le produit est disponible">
                    <button class="close-button">Fermer</button>
                    <img class="modal-picture" id="cross" src="${static}img/cross.svg" alt="Icon indiquant que le produit est indisponible">

                </div!>
            
            `

            const check = document.getElementById('ckeck')
            const cross = document.getElementById('cross')

            if (dispo == 'True') {

                check.style.visibility = "visible"
                cross.style.visibility = "hidden"

            }else{

                check.style.visibility = "hidden"
                cross.style.visibility = "visible"

            }

            modal.style.display = "flex";
            sc.style.visibility = "hidden";
            buttonTop.style.visibility = "hidden"

            const button = document.getElementsByClassName("close-button")[0];

            button.onclick = function() {
                modal.style.display = "none";
                sc.style.visibility = "visible";
                buttonTop.style.visibility = "visible"
            }

        }))

    },

    error: function (error){

        console.log(error)

    }

});

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
        sc.style.visibility = "visible";
        buttonTop.style.visibility = "visible"
    }
}