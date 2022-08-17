 function handleFunctionContact(event) {
    event.preventDefault()
    form=document.forms[0]
    console.log("Here")
    if(!form.email.value||!form.name.value||!form.message.value||!form.subject.value){
    Swal.fire('Please fill the all the fields', '', 'info')
    return;
    }
    Swal.fire({
      icon: 'success',
      title: 'Message Sent Successfully',
      showConfirmButton: true,
    }).then(() => {
        form.submit()
})
  }
function handleFunctionSell(event) {
    event.preventDefault()
    form=document.forms[0]
    if(!form.Country.value||!form.product.value||!form.State.value||!form.District.value||!form["pin-code"].value||!form.phone.value||!form.quantity.value||!form.price.value){
        Swal.fire('Please fill the all the fields', '', 'info')
        return;
    }
    Swal.fire({
      icon: 'success',
      title: 'Item Added Successfully',
      showConfirmButton: true,
    }).then(() => {
        form.submit()
})
  }
  function handleFunctionBuy(event,prodId) {
    event.preventDefault()
jQuery.ajax(
    {
        type: 'GET',
        url :"/confirm-buy?product="+prodId,
        'contentType': 'application/json',
        'dataType': 'json',
    }
)
    Swal.fire({
      icon: 'success',
      title: 'Item Bought Successfully',
      showConfirmButton: true,
    }).then((value) => {
      window.location="/option"
})
  }