var catalog = {
    products: [{
            title: "Термос",
            text: "Согреет вас холодной зимой",
            img: "img/good01.jpg",
            price: 2000
        },
        {
            title: "Кофейное зерно",
            text: "Даст здоровье и хорошее настроение",
            img: "img/good01.jpg",
            price: 15
        },
        {
            title: "Кофейная стружка",
            text: "Наполнит радостью",
            img: "img/good01.jpg",
            price: 87
        },
        {
            title: "Турка",
            text: "Сделает вам свежий кофе",
            img: "img/good01.jpg",
            price: 1500
        },
        {
            title: "Кофечай",
            text: "Уникальный напиток с горных вершин",
            img: "img/good01.jpg",
            price: 700
        },
        {
            title: "Стакан молока",
            text: "Для создания капучино и латте",
            img: "img/good01.jpg",
            price: 99
        }
    ],
    render: function (catalog_div) {
        for (let i = 0; i < catalog.products.length; i++) {
            card = document.createElement('div');
            card.classList.add('card');
            card.innerHTML = `
                            <img src="${catalog.products[i].img}" class="card-img-top">
                            <div class="card-body">
                                <h5 class="card-title">${catalog.products[i].title}</h5>
                                <p class="card-text">${catalog.products[i].text}</p>
                                <h5 class="card-title">${catalog.products[i].price} руб.</h5>
                                <a href="" class="btn btn-primary" onclick="cart.add(event,${i});">В корзину</a>
                            </div>`;
            catalog_div.appendChild(card);
        }
    }
};
var cart = {
    products: [],
    sum: 0,
    div: null,
    sum_render: function () {
        let sum_div = document.querySelector(".sum")
        if (this.sum == 0) {
            sum_div.innerHTML = "Корзина пуста";
        } else {
            sum_div.innerHTML = `<b>В корзине: ${this.products.length} товаров на сумму ${this.sum} руб.</b>`;
        }
    },
    add: function (event,id) {
        event.preventDefault();
        let item = document.createElement('div');
        item.innerHTML = `<a href="" class="btn btn-primary" onclick="cart.del(event,${id});"> - </a>${catalog.products[id].title} (${catalog.products[id].price} руб)`;
        let sum_div = document.querySelector(".sum")
        this.div.insertBefore (item,sum_div);

        this.products.push(catalog.products[id]);
        this.sum += catalog.products[id].price;
        this.sum_render();
    },
    del: function (event,id) {
        event.preventDefault();
        event.target.parentNode.remove();
        
        this.products.shift(catalog.products[id]);
        this.sum -= catalog.products[id].price;
        this.sum_render();
    },
    render: function (div) {
        this.div = div;
        this.div.innerHTML = '';
        let sum_div = document.createElement('div');
        sum_div.classList.add("sum");
        this.div.appendChild(sum_div);
        this.sum_render();
    }
};

catalog.render(document.querySelector(".catalog"));
cart.render(document.querySelector(".cart"));