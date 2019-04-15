const Width = 800;
const Heigth = 400;
const Cell_size = 20;
var hard = 1;
var anim = 300;
var anim_func;

var snake = {
    parts: [],
    direct: [0, 0],
};

var game = {
    count: 0,
    field: [],
    ongame: true,
    canvas: document.querySelector(".canvas"),
    panel: document.querySelector(".panel"),
    interval: setInterval(function () {
        game.next_move();
    }, 200),
    field_generate: function () {
        this.field = [];
        for (let i = 0; i < Heigth / Cell_size; i++) {
            let line = [];
            for (let j = 0; j < Width / Cell_size; j++) {
                line.push('');
            }
            this.field.push(line);
        };
        let x = ~~(Heigth / Cell_size / 2);
        let y = ~~(Width / Cell_size / 2);
        this.field[x][y] = 'S';
        snake.parts = [
            [x, y],
            [x - 1, y]
        ];
        snake.direct = [1, 0];
        for (let i = 0; i < hard * 3; i++) {
            this.make_obstacle();
        }
    },
    restart: function () {
        this.count = 0;
        anim = 300;
        clearInterval (anim_func);
        this.clear_canvas();

        this.field_generate();
        this.make_food();
        this.render_panel();
        window.addEventListener('keypress', game.keypress);
        this.ongame = true;
    },
    gameover: function () {
        window.removeEventListener('keypress', game.keypress);
        this.panel.innerHTML += `<h1>Game Over</h1`;
        anim = 0;
        var anim_func = setInterval(function () {
                game.make_obstacle();
                anim ++;
                if (anim > 300){
                    anim = 0;
                    clearInterval (anim_func);
                }
        }, 10);
    },
    clear_canvas: function () {
        let ctx = this.canvas.getContext("2d");
        ctx.clearRect(0, 0, Width, Heigth);
    },
    render_panel: function () {
        this.canvas.innerHTML = "";
        this.panel.innerHTML = "";
        this.panel.innerHTML = `<h3>Snake</h3>
        Управление: W,S,A,D
        <h4>Счет: ${this.count}</h4> 
        <BR><BR>Сложность:<BR>
        <div class="btn-group mr-2" role="group" aria-label="First group">
        <button type="button" class="btn btn-secondary" onclick="hard = 1;">1</button>
        <button type="button" class="btn btn-secondary" onclick="hard = 2;">2</button>
        <button type="button" class="btn btn-secondary" onclick="hard = 3;">3</button>
        <button type="button" class="btn btn-secondary" onclick="hard = 4;">4</button>
        <button type="button" class="btn btn-secondary" onclick="hard = 5;">5</button>
        </div>
        <BR><BR>
        <a href="" class="btn btn-primary" onclick="event.preventDefault();game.restart();">Restart</a>

        
    `;
    },
    next_move: function () {
        if (!this.ongame) {
            return false;
        };
        let x = snake.parts[0][0] + snake.direct[0];
        let y = snake.parts[0][1] + snake.direct[1];
        if (x > this.field.length - 1) {
            x = 0;
        };
        if (y > this.field[0].length - 1) {
            y = 0;
        };
        if (x < 0) {
            x = this.field.length - 1;
        };
        if (y < 0) {
            y = this.field[0].length - 1;
        };
        if ((this.field[x][y] == 'S') || (this.field[x][y] == 'O')) { //snake or obstacle
            this.ongame = false;
            this.gameover();
        } else if (this.field[x][y] == 'F') { //food
            this.count += 1;
            this.render_panel();
            this.field[x][y] = 'S';
            snake.parts.unshift([x, y]);
            this.render_cell(x, y, 'S');
            this.make_food();
        } else {
            this.field[x][y] = 'S';
            snake.parts.unshift([x, y]);

            let x_end = snake.parts[snake.parts.length - 1][0];
            let y_end = snake.parts[snake.parts.length - 1][1];
            this.field[x_end][y_end] = '';
            snake.parts.pop(snake.parts.length - 1);
            this.render_cell(x, y, 'S');
            this.unrender_cell(x_end, y_end);
        }
    },
    make_food: function () {
        let x, y;
        while (true) {
            y = Math.floor(Math.random() * this.field[0].length);
            x = Math.floor(Math.random() * this.field.length);
            if (this.field[x][y] == '') {
                this.field[x][y] = 'F';
                this.render_cell(x, y, 'F');
                break;
            }
        };
    },
    make_obstacle: function () {
        let x, y;
        while (true) {
            y = Math.floor(Math.random() * this.field[0].length);
            x = Math.floor(Math.random() * this.field.length);
            if (this.field[x][y] == '') {
                this.field[x][y] = 'O';
                this.render_cell(x, y, 'O');
                break;
            }
        };
    },
    render_cell: function (y, x, type) {
        let ctx = this.canvas.getContext("2d");
        if (type == 'S') {
            ctx.fillStyle = "#000000";
            ctx.fillRect(Cell_size * x, Cell_size * y, Cell_size, Cell_size);
        }
        if (type == 'F') {
            ctx.fillStyle = "#00FF00";
            ctx.fillRect(Cell_size * x, Cell_size * y, Cell_size, Cell_size);
        }
        if (type == 'O') {
            ctx.fillStyle = "#FF0000";
            ctx.fillRect(Cell_size * x, Cell_size * y, Cell_size, Cell_size);
        }
    },
    unrender_cell: function (y, x) {
        let ctx = this.canvas.getContext("2d");
        ctx.clearRect(Cell_size * x, Cell_size * y, Cell_size, Cell_size);
    },
    keypress: function (event) {
        if (event.code == 'KeyW') {
            snake.direct = [-1, 0];
        } else if (event.code == 'KeyS') {
            snake.direct = [1, 0];
        } else if (event.code == 'KeyA') {
            snake.direct = [0, -1];
        } else if (event.code == 'KeyD') {
            snake.direct = [0, 1];
        }
    }
};


game.restart();