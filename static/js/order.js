var updateBtns = document.getElementsByClassName('take-order')

for(var i=0; i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var serviceID = this.dataset.service
        var action = this.dataset.action
        console.log('serviceID:', serviceID, 'action:', action)

        console.log('USER:', user )
        if(user === 'AnonymousUser'){
            console.log("Not logged in")
        }else{
            console.log('User is Logged in...')
        }
    })
}