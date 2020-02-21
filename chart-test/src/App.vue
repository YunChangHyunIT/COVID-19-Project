<template>
  <div id="app">



    <BarChart></BarChart>
    <!-- <LineChart></LineChart> -->

    <!-- <RandomChart></RandomChart> -->
    


  </div>
</template>

<script>
import LineChart from './components/LineChart'
import BarChart from './components/BarChart'


export default {
  name: 'app',
  components: {
    LineChart,
    BarChart,
  },
  data () {
    return {
      // datacollection: {}

    }
  },
  

}//default
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
/* chart 속성 */
.small {
  max-width: 600px;
  margin:  150px auto;
}



</style>
