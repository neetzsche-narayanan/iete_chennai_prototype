function activateNewsletter(anchorEl, n){
    const arr1 = ['one_one-edition','one_two-edition','one_three-edition'];
    
    let pdfDiv = document.getElementById(arr1[n-1]);
    let activeDiv = document.querySelector('.visible')
    let activeAnchor = document.querySelector('.active')

    activeDiv.classList.toggle('visible')
    activeAnchor.classList.toggle('active')

    pdfDiv.classList.toggle('visible')
    anchorEl.classList.toggle('active')  
}

function changeBackgroundNewsletter(element){
    element.target.style.backgroundColor = '#84142D';
}