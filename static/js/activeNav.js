const menus = document.querySelectorAll('.direct')
//console.log(menus)
menus.forEach(menu => {
    //console.log(menu.classList)
    menu.onclick = function(){
        console.log(5565555)
        document.querySelector('.active').classList.remove('active')
        this.classList.add('active')
    }
})
