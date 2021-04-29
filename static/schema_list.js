new Vue({
    el: '#schema_list',
    data:{
        schemas: []
    },
    created: function () {
        const vm = this;
        axios.get('http://0.0.0.0:8000/api/schema')
            .then(function (response) {
                console.log(response.data)
                vm.schemas = response.data
            })
    }
})