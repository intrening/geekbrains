var cells = [
    ['R_B','N_B','B_B','Q_B','K_B','B_B','N_B','R_B'],
    ['P_B','P_B','P_B','P_B','P_B','P_B','P_B','P_B'],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['P_W','P_W','P_W','P_W','P_W','P_W','P_W','P_W'],
    ['R_W','N_W','B_W','Q_W','K_W','B_W','N_W','R_W']
];

renderCells();

function renderCells(){
    let line;
    let cell;
    createLineLetters (cells[0].length);
    for (let i = 0; i < cells.length; i ++){
        line = createLine();

        cell = createCell('name',i+1);
        line.appendChild(cell);
        
        for (let j = 0; j < cells[i].length; j++){
            cell = createCell(cells[i][j],'',(j+i) % 2 ==0? 'white':'black');
            line.appendChild(cell);
        }
    }
}

function createLineLetters(size_cells){
    let line = createLine();
    cell = createCell('name','')
    line.appendChild(cell);

    for (let i = 0; i < size_cells; i++){
        cell = createCell('name',String.fromCharCode(65+i));
        line.appendChild(cell);
    }
}

function createLine(){
    let line = document.createElement('div');
    line.classList.add ('line');
    
    let cells = document.getElementById('cells');
    cells.appendChild(line);
    return line;
}

function createCell (type, value, color){
    let cell = document.createElement('div');
    cell.classList.add('cell');
    if (type == "name"){
        cell.classList.add('name');
        cell.innerHTML = value;
        return cell;
    } else if (type != ''){
        cell.classList.add(type);
    }

    if (color == 'white'){
        cell.classList.add('white');
    } else if (color == 'black'){
        cell.classList.add('black');
    }

    return cell;
}

