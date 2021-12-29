function func1() {
    a = 'Racheli Eliyahu';
    console.log(a);
}

function Namevalidation() {
    var check = 0;
    for ( let i=1; i<4; i++){
        var x = "id"+i;
        console.log(x);
        var inpObj = document.getElementById(x);
        if (!inpObj.checkValidity()) {
            check = check +1 ;
            inpObjBAD = document.getElementById(x);
            console.log(check) 
        //  document.getElementById("demo").innerHTML = inpObj.validationMessage;
        } 
        // else {
        //  document.getElementById("demo").innerHTML = "Input OKK";
        // }
    
        // const inpObj2 = document.getElementById("id2");
        // if (!inpObj2.checkValidity()) {
        //  document.getElementById("demo2").innerHTML = inpObj2.validationMessage;
        // } 
        // else {
        //  document.getElementById("demo2").innerHTML = "Input OKK";
        // }
    }
    console.log("check is" ,check);
    if (check == 0 ){
        document.getElementById("demo").innerHTML = "Input OKK";
    }
    else{
        document.getElementById("demo").innerHTML = inpObjBAD.validationMessage;
        console.log("got into else");
    }

}
