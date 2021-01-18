function SValidation(){
    var age1=getElementById('G1').value;
    var age2=getElementById('G2').value;
    var age3=getElementById('G3').value;

    if(age1=='' || age2=='' ||age1==''){
        document.getElementById('gradeele').innerHTML="Please Select Age";
        false;
    }
    else{
        return true;
    }
}



var overlay = document.getElementById("overlay");

window.addEventListener('load', function() {
    overlay.style.display = 'none';
})
var db = document.getElementById("db");
var full = "jakhar";
window.addEventListener('load', function() {
    db.style.display = 'block';
})

