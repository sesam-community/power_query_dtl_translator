<template>
    <div id="Speed" v-on:keyup.enter="insertData">
        <h1>Power Query to SESAM DTL Converter</h1>
        <input name="pbiInput" ref='pbiInput' value="Paste in your Power Query code snippet here..." id="pbiInput">
        <br>
        <button v-on:click.prevent="insertData">Submit query and make DTL</button>
        <br>
        <img v-if='isLoading' src="https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif" alt="Loading GIF">
        <input v-if="isInputVis" id="dtlCode">
    </div>
</template>

<script>
import api from '../api'
export default {
    name: 'Speed',
    data: () => {
        return {
            isInputVis : false,
            isLoading : false,
            rows : {
                repository_name: '{{repository_name}}',
                created_at: '{{created_at}}',
                latest_push: '{{latest_push}}'
            }  
        }
    },
    methods: {
        insertData(){ 
          let pbiInput = this.$refs.pbiInput.value
          fetch('http://localhost:5000/query', {
            method: 'POST',
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json'
        },
        body: JSON.stringify({pbiInput: pbiInput})
        });
        this.$refs.pbiInput.value = []
        this.pasteData()
        },
        pasteData(){
            this.isLoading = true
            api.getResource('/dtl_transform')
                .then((data) => {
                // eslint-disable-next-line no-console
                //console.log(data)
            this.isInputVis = true    
            let dtlCode = data
            console.log(data)
            this.isLoading = false
            })
        }    
    }    
}
</script>

<style scoped>
h1 {
    color: blue;
}
table {
    margin: auto;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    margin: center;
}

table th {
  text-transform: uppercase;
  font-size: 17px;
  color: blue;
  padding: 10px;
  min-width: 30px;
  border-bottom: 2px solid #7D82A8;
  border: 2px;
}

table td {
  padding: 8px;
}

table tbody td {
  border: 1px solid#7D82A8;
}

#pbiInput {
      text-align: center;
      width:60%;
      height:300px;
      padding:5px 10px;
      font-size: 12px;
      color: black;
      letter-spacing:1px;
      background: #FFF;
      border:2px solid #FFF;
      margin-bottom:25px;
      -webkit-transition:all .1s ease-in-out;
      -moz-transition:all .1s ease-in-out;
      -ms-transition:all .1s ease-in-out;
      -o-transition:all .1s ease-in-out;
      transition:all .1s ease-in-out;
}

#dtlCode {
    text-align: center;
      width:60%;
      height:500px;
      padding:5px 10px;
      font-size: 12px;
      color: black;
      letter-spacing:1px;
      background: #FFF;
      border:2px solid #FFF;
      margin-bottom:25px;
      -webkit-transition:all .1s ease-in-out;
      -moz-transition:all .1s ease-in-out;
      -ms-transition:all .1s ease-in-out;
      -o-transition:all .1s ease-in-out;
      transition:all .1s ease-in-out;
}

button {
      width:20%;
      padding:5px 10px;
      font-size: 12px;
      letter-spacing:1px;
      background:blue;
      height:40px;
      text-transform:uppercase;
      letter-spacing:1px;
      color:#FFF;
      -webkit-transition:all .1s ease-in-out;
      -moz-transition:all .1s ease-in-out;
      -ms-transition:all .1s ease-in-out;
      -o-transition:all .1s ease-in-out;
      transition:all .1s ease-in-out;
}

</style>
