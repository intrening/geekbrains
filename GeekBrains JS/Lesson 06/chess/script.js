var cells = [
    ['R_B', 'N_B', 'B_B', 'Q_B', 'K_B', 'B_B', 'N_B', 'R_B'],
    ['P_B', 'P_B', 'P_B', 'P_B', 'P_B', 'P_B', 'P_B', 'P_B'],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['P_W', 'P_W', 'P_W', 'P_W', 'P_W', 'P_W', 'P_W', 'P_W'],
    ['R_W', 'N_W', 'B_W', 'Q_W', 'K_W', 'B_W', 'N_W', 'R_W']
];

renderCells();

function renderCells() {
    let line;
    let cell;
    createLineLetters(cells[0].length);
    for (let i = 0; i < cells.length; i++) {
        line = createLine();

        cell = createCell('name', i + 1);
        line.appendChild(cell);

        for (let j = 0; j < cells[i].length; j++) {
            cell = createCell(cells[i][j], '', (j + i) % 2 == 0 ? 'white' : 'black');
            line.appendChild(cell);
        }
    }

    function createLineLetters(size_cells) {
        let line = createLine();
        cell = createCell('name', '')
        line.appendChild(cell);

        for (let i = 0; i < size_cells; i++) {
            cell = createCell('name', String.fromCharCode(65 + i));
            line.appendChild(cell);
        }
    }

    function createLine() {
        let line = document.createElement('div');
        line.classList.add('line');

        let cells = document.getElementById('cells');
        cells.appendChild(line);
        return line;
    }

    function createCell(type, value, color) {
        let cell = document.createElement('div');
        cell.classList.add('cell');

        if (color == 'white') {
            cell.classList.add('white');
        } else if (color == 'black') {
            cell.classList.add('black');
        }

        if (type == "name") {
            cell.classList.add('name');
            cell.innerHTML = value;
        } else if (type != '') {
            var figure = document.createElement('img');
            figure.classList.add('figure');
            figure.style.zIndex = -1;
            figure.classList.add(type);
            figure.onclick = figure_mousedown;
            cell.appendChild(figure);
        }

        return cell;
    }
}

var figure_active;
var figure_parent;

function figure_mousedown(element) {
    figure_active = element.target;
    figure_parent = element.target.parentNode;
    figure_active.style.position = 'absolute';
    moveAt(element);
    figure_active.style.zIndex = 1000;
    figure_active.ondragstart = function () {
        return false;
    };

    document.body.appendChild(figure_active);

    document.onmousemove = function (element) {
        if (figure_active) {
            moveAt(element);
        };
        
    };
    document.onmouseup = function (element) {
        document.onmousemove = null;
        document.onmouseup = null;
        figure_active.style.position = '';
        if (isFreeCell(element)){
            isFreeCell(element).appendChild(figure_active);   
        }  else {
            figure_parent.appendChild(figure_active);
        };
        figure_active = null;
        figure_parent = null;
    };
};

function moveAt(element) {
    figure_active.style.left = element.pageX - figure_active.offsetWidth / 2 + 'px';
    figure_active.style.top = element.pageY - figure_active.offsetHeight / 2 + 'px';
};

var isFreeCell = function (element){
    var cell = document.elementFromPoint(element.clientX, element.clientY);
    if (cell == figure_parent){
        return false;
    }
    if (cell.classList.contains('figure')){
        return false;
    };
    if (cell.querySelectorAll('.figure').length > 0){
        return false;
    }
    return cell;
};