class GoodsItem {
    constructor(title = '', price = 0, text = '', img = '') {
        this.title = title;
        this.price = price;
        this.text = text;
        this.img = img;
    };
    render() {
        return `
        <div class="card">
        <img src="${this.img}" class="card-img-top">
        <div class="card-body">
            <h5 class="card-title">${this.title}</h5>
            <p class="card-text">${this.text}</p>
            <h5 class="card-title">${this.price} руб.</h5>
            <a href="" class="btn btn-primary" onclick="">В корзину (не работает)</a>
        </div>
        </div>
        `;
    }
};

class GoodsList {
    constructor() {
        this.goods = [];
    }
    fetchGoods() {
        this.goods.push(new GoodsItem('Термос', 199, 'шикарное описание термоса', 'img/good01.jpg'));
        this.goods.push(new GoodsItem('Кофечай', 999, 'шикарное описание кофечая', 'img/good02.jpg'));
        this.goods.push(new GoodsItem('Турка', 499, 'шикарное описание турки', 'img/good01.jpg'));
    }
    render() {
        let listHtml = `<h3>Общая стоимость продуктов: ${this.sum()} руб.</h3>`;
        this.goods.forEach(goodItem => {
            listHtml += goodItem.render();
        });
        document.querySelector('.catalog').innerHTML = listHtml;
    }
    sum() {
        let sum = 0;
        this.goods.forEach(goodItem => {
            sum += goodItem.price;
        });
        return sum;
    }

}
class Cart {
    constructor() {
        this.products = [];
        this.sum = 0;
        this.div = document.querySelector(".cart");
    }
    sum_render() {
        let sum_div = document.querySelector(".sum")
        if (this.sum == 0) {
            sum_div.innerHTML = "Корзина пуста и не работает";
        } else {
            sum_div.innerHTML = `<b>В корзине: ${this.products.length} товаров на сумму ${this.sum} руб.</b>`;
        }
    };
    // add(event, id) {
    //     event.preventDefault();
    //     let item = document.createElement('div');
    //     item.innerHTML = `<a href="" class="btn btn-primary" onclick="cart.del(event,${id});"> - </a>${catalog.products[id].title} (${catalog.products[id].price} руб)`;
    //     let sum_div = document.querySelector(".sum")
    //     this.div.insertBefore(item, sum_div);

    //     this.products.push(catalog.products[id]);
    //     this.sum += catalog.products[id].price;
    //     this.sum_render();
    // };
    // del(event, id) {
    //     event.preventDefault();
    //     event.target.parentNode.remove();

    //     this.products.shift(catalog.products[id]);
    //     this.sum -= catalog.products[id].price;
    //     this.sum_render();
    // };
    render(div) {
        this.div.innerHTML = '';
        let sum_div = document.createElement('div');
        sum_div.classList.add("sum");
        this.div.appendChild(sum_div);
        this.sum_render();
    };
};


let goodlist = new GoodsList();
goodlist.fetchGoods();
goodlist.render();

let cart = new Cart();
cart.render();