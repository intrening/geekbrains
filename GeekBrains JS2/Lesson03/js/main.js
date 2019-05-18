const API = 'https://raw.githubusercontent.com/GeekBrainsTutorial/online-store-api/master/responses';

class ProductsList {
    constructor() {
        this.products = [];
        this.allProducts = [];
        this.init();
        this.cartProducts = [];
    }
    init() {
        this._getProducts();
    }

    _getProducts() {
        fetch(`${API}/catalogData.json`)
            .then(result => result.json())
            .then(data => {
                this.products = [...data];
                this.render()
            })
            .catch(error => {
                console.log(error)
            })
    }
    getProductbyId(id) {
        //console.log(this.products)
        let product_selected;
        this.products.forEach(product => {
            if (product.id_product == id) {
                product_selected = product;
            }
        })
        return product_selected;
    }
    render() {
        const block = document.querySelector('.products');
        this.products.forEach(product => {
            const prod = new Product(product);
            this.allProducts.push(prod);
            block.insertAdjacentHTML('beforeend', prod.render())
        })
    }
    sumPrice() {
        return this.allProducts.reduce((accum, item) => accum += item.price, 0);
    }
}

class Cart {
    constructor() {
        this.products = [];
        this.sum = 0;
        this.div = null;
        this.render()
    }
    _sum_render() {
        let sum_div = document.querySelector(".sum")
        if (this.sum == 0) {
            sum_div.innerHTML = "Корзина пуста";
        } else {
            sum_div.innerHTML = `<b>В корзине: ${this.products.length} товаров на сумму ${this.sum} $.</b>`;
        }
    }
    add(prod_id) {
        let product = products.getProductbyId(prod_id.getAttribute("data-id"));
        this.products.push(product)
        this.sum += product.price;
        this.render();
    }
    del(event, num) {
        event.preventDefault();
        //event.target.parentNode.remove();
        this.sum -= this.products[num].price;
        this.products.splice(num,1)
        console.log(num)
        console.log(this.products)
        this.render();
    }
    render() {
        this.div = document.querySelector(".cart");
        this.div.innerHTML = '';
        let sum_div = document.createElement('div');
        sum_div.classList.add("sum");
        this.div.appendChild(sum_div);

        //let num = this.products.length-1;
        let sum_div_find = document.querySelector(".sum")

        for (let num = 0; num < this.products.length; num++) {
            let item = document.createElement('div');
            item.innerHTML = `<a href="" class="btn btn-primary" onclick="cart.del(event,${num});"> - </a>${this.products[num].product_name} (${this.products[num].price} $)`;
            this.div.insertBefore(item, sum_div_find);  
        }
        this._sum_render();
    }
}

class Product {
    constructor(product, img = 'https://placehold.it/200x150') {
        this.product_name = product.product_name;
        this.price = product.price;
        this.id_product = product.id_product;
        this.img = img
    }
    render() {
        return `<div class="product-item">
                    <img src="${this.img}" alt="Some img">
                    <div class="desc">
                        <h3>${this.product_name}</h3>
                        <p>${this.price} $</p>
                        <button class="buy-btn" data-id="${this.id_product}" onclick="cart.add(this);">Купить</button>
                    </div>
                </div>`
    }
}

let products = new ProductsList();
let cart = new Cart();

//console.log(products.sumPrice());