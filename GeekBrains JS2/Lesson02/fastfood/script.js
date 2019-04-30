'use strict'

let stuffing_all = {
    cheese: {
        name: 'cheese',
        price: 10,
        calories: 20
    },
    salad: {
        name: 'salad',
        price: 20,
        calories: 5
    },
    potato: {
        name: 'potato',
        price: 15,
        calories: 10
    }
}
let toppings = {
    pepper: {
        name: 'pepper',
        price: 15,
        calories: 0
    },
    mai: {
        name: 'mai',
        price: 20,
        calories: 5
    }
}

class Hamburger {
    constructor(size, stuffing) {
        this.size = size;
        this.stuffing = stuffing_all[stuffing];
        this.topping_list = [];
        if (size == 'small') {
            this.price = 50;
            this.calories = 20;
        } else {
            this.price = 100;
            this.calories = 40;
        }
    }
    addTopping(topping) {
        this.topping_list.push(topping);
    }
    removeTopping(topping) {
        let index = this.topping_list.indexOf(topping);
        delete this.topping_list[index];
    }
    getToppings() {
        let str = '';
        this.topping_list.forEach(function (value) {
            str += value.name + ' ';
        });
        return str;
    }
    getSize() {
        return this.size;
    }
    getStuffing() {
        return this.stuffing.name;
    }
    calculatePrice() {
        let sum = this.price + this.stuffing.price;

        this.topping_list.forEach(function (value) {
            sum += value.price;
        });
        return sum;
    }

    calculateCalories() {
        let sum = this.calories + this.stuffing.calories;

        this.topping_list.forEach(function (value) {
            sum += value.calories;
        });
        return sum;
    }
}

function checkout(size, stuffing, pepper, mai) {
    var hamb = new Hamburger(size, stuffing);

    if (pepper) hamb.addTopping(toppings['pepper']);
    if (mai) hamb.addTopping(toppings['mai']);

    renderCart(hamb);
    return false;
}

function renderCart(hamb) {
    let str = `
    Размер: ${hamb.size}<br>
    Начинка: ${hamb.getStuffing()}<br>
    Топпинги: ${hamb.getToppings()}<br>
    Стоимость:${hamb.calculatePrice()}<br>
    Калорийность:${hamb.calculateCalories()}<br>
    `;
    document.querySelector('.cart').innerHTML = str;
}