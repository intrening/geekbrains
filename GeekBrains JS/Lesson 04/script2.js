var round = 0;
var questions = [
    {
        text: 'Где, если верить пословице, любопытной Варваре нос оторвали?',
        answer1: 'На вокзале',
        answer2: 'На базаре',
        answer3: 'На фонтане',
        answer4: 'В спортзале',
        right: '2'
    },
    {
        text: 'Кто автор «Сказки о попе и работнике его Балде»?',
        answer1: 'Пушкин',
        answer2: 'Лермонов',
        answer3: 'Достоевский',
        answer4: 'Ленин',
        right: '1'
    },
    {
        text: 'Исполнитель роли Бендера в «Золотом теленке»?',
        answer1: 'Папанов',
        answer2: 'Юрский',
        answer3: 'Миронов',
        answer4: 'Козловский',
        right: '2'
    },
    {
        text: 'В каком году Россия объявила дефолт?',
        answer1: '1991',
        answer2: '1986',
        answer3: '1998',
        answer4: '2008',
        right: '3'
    }
];

window.onload = function () {
    game_restart();
};

function game_restart() {
    round = 0;
    generateQuestion();
}

function game_finish(win) {
    if (win) {
        alert('Вы победили!');
    } else {
        alert('Неверно! Вы проиграли!');
    }
    game_restart();
};

function getAnswer(answer) {
    if (answerIsRight(answer)){
        generateQuestion();
    } else {
        game_finish(false);
    }
};

function generateQuestion() {
    if (round < questions.length) {
        var question = document.getElementById('question');
        var answer1 = document.getElementById('answer1');
        var answer2 = document.getElementById('answer2');
        var answer3 = document.getElementById('answer3');
        var answer4 = document.getElementById('answer4');
        var round_text = document.getElementById('round');

        question.innerHTML = questions[round]['text'];
        answer1.innerHTML = questions[round]['answer1'];
        answer2.innerHTML = questions[round]['answer2'];
        answer3.innerHTML = questions[round]['answer3'];
        answer4.innerHTML = questions[round]['answer4'];

        round++;
        round_text.innerHTML = "Раунд: " + round + ' из ' + questions.length;
    } else {
        game_finish(true);
    };
};

function answerIsRight(answer) {
    if (questions[round - 1]['right'] == answer) {
        return true;
    } else {
        return false;
    }
};