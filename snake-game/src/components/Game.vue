<template>
    <div id="game-area">
        <canvas id="game-canvas" ref="canvas" width="200" height="200"></canvas>
        <span>Length: {{ this.length }}</span>
    </div>
</template>
<script>

export default {
    data: function() {
        return {
            size: 20,
            length: 5,
            trail: [],
            velocity: 1,
            direction: this.keyDownEvent,
            canvasContext: null,
            cellSize: 10,
            frameRate: 100, // ms
            egg: {
                position: [0, 0],
                radius: 3,
                status: 0, // 0 is available, 1 is eaten
            },
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
            this.trail.push(nextMove);

            if (nextMove[0] == this.egg.position[0] && nextMove[1] == this.egg.position[1]) {
                this.generateNewEgg();
                this.length += 1;
            } else {
                this.trail.shift();
            }

            this.render();
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
            this.canvasContext.fillStyle="red";
            this.canvasContext.fill()
        }
    },
    watch: {
        keyDownEvent: function(direction, _) {
            this.onKeyDown(...direction);
        }
    },
    mounted: function() {
        this.initializeGame();
        setInterval(this.nextFrame, this.frameRate);
    },
}
</script>

<style scoped>
#game-canvas {
    display: inline-block;
    padding: 0 0 0 0;
    border: 1px solid black;
}
</style>
