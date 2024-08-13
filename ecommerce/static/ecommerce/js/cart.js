var updateCart = document.getElementsByClassName("update_cart")


for (let index = 0; index < updateCart.length; index++) {
     updateCart[index].addEventListener("click", function() {
        this.preventDefault
       let productID = this.dataset.product;
       let action = this.dataset.action;

       let context = {
         ID: productID,
         action: action,
       };

       updateItem(productID, action)
     });
    
}


function updateItem(ID, act) {
    
   var url = "/shop/UpdateItem/";

   fetch(url, {
     method: "POST",
     headers: { "Content-Type": "application/json", 
     "X-CSRFToken": token },
     
     body: JSON.stringify({ productID: ID, action: act }),
   })
     .then((response) => {
       return response.json();
     })

     .then((data) => {
       console.log("data", data);
     });

     console.log(token)
}

