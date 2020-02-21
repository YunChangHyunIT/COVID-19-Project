<template>
  <div class="small">
    <bar-chart :chart-data="datacollection"></bar-chart>
    <button @click="DataSet()">데이터설정</button>
    <button @click="coronafillData()">코로나차트그리기</button>
    <button @click="maskfillData()">마스크차트그리기</button>

  </div>
</template>

<script>
import BarChart from '../chart_group/BarChart'


export default {
  components: {
    BarChart,
  },
  data () {
    return {
      datacollection: {},
      coronadata: [],
      maskData: [],
      coronaName: '',
      coronadate: [],
      coronacount: [],
      maskName: '',
      maskdate: [],
      maskcount: []
    }
  },
  mounted () {
    this.getdata('corona')
    this.getdata('mask')
  },
  methods: {
    DataSet() {
      
      
      this.coronadata.result.forEach( data =>{
        this.coronaName = data.search_name
        this.coronadate.push(data.date)
        this.coronacount.push(data.count)
      })

      this.maskData.result.forEach( data =>{
        this.maskName = data.search_name
        this.maskdate.push(data.date)
        this.maskcount.push(data.count)
      })
      // console.log(this.coronadata)
      // console.log(this.coronadata)
      // this.coronadata.forEach(data => {
      //   this.coronaName = data.search_name
      //   this.coronadate.push(data.date)
      //   this.coronacount.push(data.count)
      // });
    },
    coronafillData () {
      this.datacollection = {
        labels: this.coronadate,
        datasets: [
          {
            label: this.coronaName,
            backgroundColor: '#f87979',
            data: this.coronacount
          }
        ]
      }
    },
    maskfillData () {
      this.datacollection = {
        labels: this.maskdate,
        datasets: [
           {
            label: this.maskName,
            backgroundColor: '#f87979',
            data: this.maskcount
          }
        ]
      }
    },
    getRandomInt () {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5
    },
    getdata(searchWord) {
      const address = 'http://127.0.0.1:8000/' + searchWord + '/'
      console.log(address)
      this.$http.get(address).then((res) => {
      if(res.data != null && res.data.length !== 0)
      {
        if(searchWord == 'corona')
        {
          this.coronadata = res.data
        }
        else if (searchWord == 'mask')
          this.maskData = res.data
      } else {
        if(searchWord == 'corona')
        {
          this.coronadata = []
        }
        else if (searchWord == 'mask')
          this.maskData = []
      }
    })
    }
  }
}
</script>

<style>
.small {
  max-width: 600px;
  margin:  150px auto;
}
</style>