window.onload = function () {

    const cartItems = document.querySelectorAll('.cart-item')
    const totalValueFields = document.querySelectorAll('.total-value')
    const finalPrice = document.querySelector('.final-price')

    const getFinalPrice = function () {
        let finalPrice = 0
        
        totalValueFields.forEach(field => {
            finalPrice += parseFloat(field.innerHTML)
            
        })  
        return finalPrice.toFixed(2)
    }
    
    cartItems.forEach(cartItem => {

        const priceField = cartItem.querySelector('.product-price')
        const quantityField = cartItem.querySelector('.product-quantity')
        const plusBtn = cartItem.querySelector('.btn-plus')
        const minusBtn = cartItem.querySelector('.btn-minus')
        const totalValue = cartItem.querySelector('.total-value')

        
        

        const updatePrice = function () {
            updatedValue = (priceField.innerHTML * quantityField.value).toFixed(2)
            return updatedValue
        }

        totalValue.innerHTML = updatePrice()
        
        plusBtn.addEventListener('click', (e) => {
            e.preventDefault()
            totalValue.innerHTML = updatePrice() 
            finalPrice.innerHTML = getFinalPrice()
        })
        minusBtn.addEventListener('click', (e) => {
            e.preventDefault()
            totalValue.innerHTML = updatePrice() 
            finalPrice.innerHTML = getFinalPrice()
        })

        finalPrice.innerHTML = getFinalPrice()
    })

    

}