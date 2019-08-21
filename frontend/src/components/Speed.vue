<template>
    <div id="Speed" v-on:keyup.enter="insertData">
        <h1>SESAM Config Diagnostics Center</h1>
        <input name="tokenInput" ref='tokenInput' value="Type in your access token for Github Authentification">
        <br>
        <button v-on:click.prevent="insertData">Submit token and perform scan</button>
        <br>
        <img v-if='isLoading' src="https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif" alt="Loading GIF">
        <table v-if="isTableVis">
        <thead>
            <tr>
                <th>Github repository</th>
                <th>Created at</th>
                <th>Latest push</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="index in rows" v-bind:key="index.repository_name+index.created_at">
                    <td>{{index.repository_name}}</td>
                    <td>{{index.created_at}}</td>
                    <td>{{index.latest_push}}</td>
            </tr>
        </tbody>
        </table>
    </div>
</template>

<script>
import api from '../api'
export default {
    name: 'Speed',
    data: () => {
        return {
            isTableVis : false,
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
          let tokenInput = this.$refs.tokenInput.value
          fetch('http://localhost:5000/token', {
            method: 'POST',
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json'
        },
        body: JSON.stringify({tokenInput: tokenInput})
        });
        this.$refs.tokenInput.value = []
        this.pasteData()
        },
        pasteData(){
            this.isLoading = true
            api.getResource('/get_statistics')
                .then((data) => {
                // eslint-disable-next-line no-console
                //console.log(data)
            this.isTableVis = true    
            this.rows = data
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

input {
      text-align: center;
      width:35%;
      height:30px;
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
      width:15%;
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
