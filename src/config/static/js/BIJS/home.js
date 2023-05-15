function consultar(){
    
    axios.get('https://api.github.com/user',{
//datos
    }, {
        headers: {
            'Authorization': `token ${access_token}`
        }
    })
    .then((res) => {
        console.log(res.data)
    })
    .catch((error) => {
        console.error(error)
    })
}

/*
const {data} = await axios.post('https://httpbin.org/post', {
    firstName: 'Fred',
    lastName: 'Flintstone',
    orders: [1, 2, 3],
    photo: document.querySelector('#fileInput').files
  }, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  }
)
*/