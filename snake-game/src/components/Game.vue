<template>
    <div id="game-area">
        <div id="difficulty-slider">
            <div>
                <span>Difficulty</span>
            </div>
            <vue-slider
                v-model="difficulty.level"
                :min="1"
                :max="5"
                :interval="1"
                :adsorb="true"
                @change="changeDifficulty"
                width="200px"
            >
            </vue-slider>
        </div>
        <canvas id="game-canvas" ref="canvas" width="200" height="200"></canvas>
        <div>
            <span>Current score: {{ score.currentScore }}</span>
            <br />
            <span>Best: {{ score.maxScore }}</span>
        </div>
    </div>
</template>
<script>
import VueSlider from 'vue-slider-component';
import 'vue-slider-component/theme/default.css';
import { setInterval } from 'timers';

export default {
    components: {
        VueSlider
    },
    data: function() {
        return {
            size: 20,
            length: 5,
            trail: [],
            velocity: 1,
            direction: this.keyDownEvent,
            canvasContext: null,
            ticker: null,
            cellSize: 10,
            frameRate: 150, // ms [1000, 50]
            egg: {
                position: [0, 0],
                radius: 3,
            },
            difficulty: {
                level: 3, // 1 to 10
                frameRates: [250, 200, 150, 100, 50],
            },
            score: {
                currentScore: 0,
                maxScore: 0,
            }
        };
    },
    props: [
        'keyDownEvent'
    ],
    methods: {
        initializeGame() {
            this.canvasContext = this.$refs.canvas.getContext('2d');

            for (let i = 0; i < this.length; ++i) {
                this.trail.push([0, i]);
            }
            this.render();

            this.renderEgg(10, 10);
        },
        getNextMove() {
            let x = this.trail[this.length - 1][0], y = this.trail[this.length - 1][1];
            x += this.velocity * this.direction[0] + this.size;
            y += this.velocity * this.direction[1] + this.size;
            return [x % this.size, y % this.size];
        },
        updateTrail() {
            let nextMove = this.getNextMove();
            this.checkAndChopTail(nextMove);
            this.trail.push(nextMove);

            if (nextMove[0] == this.egg.position[0] && nextMove[1] == this.egg.position[1]) {
                this.generateNewEgg();
                this.length += 1;
                this.updateCurrentScore();
            } else {
                this.trail.shift();
            }

            this.render();
        },
        updateCurrentScore() {
            this.score.currentScore = this.length;
        },
        updateMaxScore() {
            this.score.maxScore = Math.max(this.score.maxScore, this.score.currentScore);
        },
        checkAndChopTail(nextMove) {
            let foundIdx = -1;
            for (let i = 0; i < this.length; ++i) {
                if (nextMove[0] == this.trail[i][0] && nextMove[1] == this.trail[i][1]) {
                    foundIdx = i;
                }
            }
            if (foundIdx != -1) {
                this.trail = this.trail.splice(foundIdx + 1);
                this.length = this.trail.length;

                this.updateMaxScore();
                this.updateCurrentScore();
            }
        },
        onKeyDown(dx, dy) {
            if (this.direction[0] + dx != 0 && this.direction[1] + dy != 0) {
                this.direction = [dx, dy];
            }
        },
        nextFrame() {
            this.updateTrail();
        },
        generateNewEgg() {
            let randX = Math.floor(Math.random() * Math.floor(this.size)),
                randY = Math.floor(Math.random() * Math.floor(this.size));
            
            this.egg.position = [randX, randY];
        },
        render() {
            this.canvasContext.fillStyle = 'white';
            this.canvasContext.fillRect(
                0, 0,
                this.size * this.cellSize, this.size * this.cellSize
            );

            for (let i = 0; i < this.length; ++i) {
                const cellTopLeft = this.trail[i];
                this.renderCell(this.cellSize * cellTopLeft[0], this.cellSize * cellTopLeft[1]);
            }
            this.renderEgg();
        },
        renderCell(x, y) {
            this.canvasContext.fillStyle = 'black';
            this.canvasContext.fillRect(
                x + 1, y + 1,
                this.cellSize - 1, this.cellSize - 1
            );
        },
        renderEgg() {
            let cx = this.egg.position[0] * this.cellSize + this.cellSize / 2,
                cy = this.egg.position[1] * this.cellSize + this.cellSize / 2;

            this.canvasContext.beginPath();
            this.canvasContext.arc(cx, cy, this.egg.radius, 0, 2 * Math.PI);
            this.canvasContext.stroke();
            this.canvasContext.fillStyle = "green";
            this.canvasContext.fill()
        },
        changeDifficulty() {
            this.frameRate = this.difficulty.frameRates[this.difficulty.level - 1];
            this.ticker.close();
            this.ticker = setInterval(this.nextFrame, this.frameRate);
        },
    },
    watch: {
        keyDownEvent: function(direction) {
            this.onKeyDown(...direction);
        }
    },
    mounted: function() {
        this.initializeGame();
        this.ticker = setInterval(this.nextFrame, this.frameRate);
    },
}
</script>

<style scoped>
#game-area {
    width: 250;
}

#game-canvas {
    display: inline-block;
    padding: 0 0 0 0;
    border: 1px solid black;
}

#difficulty-slider {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 10px 0px;
}
</style>
