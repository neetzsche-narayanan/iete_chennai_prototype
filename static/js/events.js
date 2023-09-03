
function eventModalOpen(anchorEl){
    let className = anchorEl.getAttribute("Class");
    let mod = document.getElementById(className);
    let heroSec = document.getElementById('hero-bg');
    let mainCont = document.getElementById('main-container');


    console.log(className);
    console.log(mod);

    console.log(heroSec.getAttribute("Class"))
    if(heroSec.getAttribute("Class") == "hero-bg modalOpen"){
        let alreadyActive = document.querySelector('.visible');
        console.log(alreadyActive);
        
        if(alreadyActive == mod){
            return;
        }else{
            alreadyActive.classList.toggle('visible');
            mod.classList.toggle('visible');
            return;
        }
    }

    mod.classList.toggle('visible');
    heroSec.classList.toggle('modalOpen');
    console.log(mainCont.style.backgroundColor);
    mainCont.style.backgroundColor = 'var(--dark-vanilla)';
    console.log(mainCont.style.backgroundColor);
};

function eventModalClose(anchorEl){ 
    let mod = anchorEl.closest('.event-modal-container');
    let heroSec = document.getElementById('hero-bg');
    let mainCont = document.getElementById('main-container');


    mod.classList.toggle('visible');
    heroSec.classList.toggle('modalOpen');
    mainCont.style.backgroundColor = 'var(--cornsilk)';
};


