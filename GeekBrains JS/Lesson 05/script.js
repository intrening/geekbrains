var size_cells = 8;
window.onload = gameLoad;


function gameLoad(){
    renderCells();
    renderFigures();
}

function renderFigures(){
    let lines = document.getElementsByClassName('line');
    for (let i in lines.namedItem){
        console.log(i);
    }
}

function renderCells(){
    let line;
    createLineLetters (size_cells);
    for (let i = 0; i < size_cells; i ++){
        line = createLine();
        createCell(line, i+1);
        for (let j = 0; j < size_cells; j++){
            createCell(line, (j+i) % 2 ==0? 'white':'black');
        }
    }
}

function createLineLetters(){
    let line = createLine();
    createCell(line, '');
    for (let i = 0; i < size_cells; i++){
        createCell(line, 'name',String.fromCharCode(65+i));
    }
}

function createLine(){
    let line = document.createElement('div');
    line.classList.add ('line');
    
    let cells = document.getElementById('cells');
    cells.appendChild(line);
    return line;
}

function createCell (line, type, value,){
    let cell = document.createElement('div');
    cell.id = value;
    cell.classList.add('cell');

    if (type == 'white'){
        cell.classList.add('white');
    } else if (type == 'black'){
        cell.classList.add('black');
    } else if (type == 'name'){
        cell.classList.add('name');
        cell.innerHTML = value;
    }
    line.appendChild (cell);
}