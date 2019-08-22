<template>
    <div id="Speed" v-on:keyup.enter="insertData">
        <h1>Power Query to DTL Converter</h1>
        <textarea name="pbiInput" ref='pbiInput' placeholder="Paste in your code snippet here..." id="pbiInput"></textarea>
        <br>
        <button v-on:click.prevent="insertData">Submit query and make DTL</button>
        <br>
        <img v-if='isLoading' src="https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif" alt="Loading GIF">
        <br>
        <!--<textarea v-if="isInputVis" id="dtlCode" v-model="rows.object" class="form-control"></textarea>-->
        <!--<span v-if="isInputVis">{{rows.object}}</span>-->
        <div v-if="isInputVis">
            <h3>{{ rows }}</h3> 
            <h4>Copy the above generated code snippet and paste in SESAM when constructing your pipe config in the transform section</h4>
        </div>
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
                object: "{{transform}}"
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

h3 {
    text-align: center;
    white-space: nowrap;
    word-break: initial;
}

#pbiInput {
      text-align: center;
      width:60%;
      height:200px;
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
