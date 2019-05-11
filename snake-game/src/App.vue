<template>
  <div id="app">
    <GlobalEvents
        @keydown.up="onKeyDown(0, -1)"
        @keydown.right="onKeyDown(1, 0)"
        @keydown.down="onKeyDown(0, 1)"
        @keydown.left="onKeyDown(-1, 0)">
    </GlobalEvents>
    <Game 
      v-bind:keyDownEvent="keyDownEvent"
    />
  </div>
</template>

<script>
import Game from './components/Game.vue';
import GlobalEvents from 'vue-global-events';

export default {
  name: 'app',
  components: {
    GlobalEvents,
    Game,
  },
  data: function() {
    return {
      keyDownEvent: [1, 0]
    }
  },
  methods: {
    onKeyDown(x, y) {
      this.keyDownEvent = [x, y]
    }
  }
}
</script>
   
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
