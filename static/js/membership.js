function roleModalOpen(x){
    const arr = ['hf','df','f','m','am','a','org','dip','amiete']
    let mod = document.getElementById(arr[x]);
    let mainCont = document.getElementById('main-container');

    mod.classList.toggle('visible');
    mainCont.classList.toggle('blur');

};

function closeModal(x){ //For membership section
    const arr = ['hf','df','f','m','am','a','org','dip','amiete']
    let mod = document.getElementById(arr[x]);
    let mainCont = document.getElementById('main-container');

    mod.classList.toggle('visible');
    mainCont.classList.toggle('blur');
};


