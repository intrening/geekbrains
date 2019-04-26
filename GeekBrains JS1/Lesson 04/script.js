function numToObj() {
    num = document.forms["form"].elements["num"].value;
    if (isNumber(num)){
        obj.update(num);
        console.log(obj);
    } else {
        alert (num + ' это не число от 0 до 999!');
    }
    return false;
}


function isNumber (num){
    if (num >= 0 && num <=999){
        return true;
    } else {
        return false;
    }
}

var obj = {
    ones: 0,
    tens: 0,
    huns: 0,
    update: function (num){
        this.ones = num % 10;
        this.tens = (num % 100 - this.ones)/10;
        this.huns = (num % 1000 - this.tens*10 - this.ones)/100;
    }
}

