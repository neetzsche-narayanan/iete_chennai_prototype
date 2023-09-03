const eventDate = document.getElementById('event-date').innerText;

const dateEvent = new Date(eventDate);
const dateNow = new Date();

const diffTime = (dateEvent - dateNow);
const diffDays = Math.floor(diffTime / (1000*3600*24));

if(diffDays >= 0){
    let daysDiv = document.getElementById('days-remaining');
    daysDiv.innerHTML = "<p><b>Days until the event starts: </b>" + diffDays.toString() + "</p>";
}