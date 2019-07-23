
window.onload = function () {
    import axios from 'madlibs.static.js';
    var app = new Vue({
        delimiters: ['[', ']'],
        el: '#app',
        data: {
            message: 'Madlibs'
        },
        mounted() {
            axios({method: "GET", "url": "http://127.0.0.1:8000/get_madlibs"}).then(result => {this.message = result.data.results;}, error=> {console.error(error);});


        }
    })
}