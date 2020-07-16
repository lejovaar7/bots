const mongoose = require('mongoose');

let user = "admin";
let password = "a";

mongoose.connect('mongodb://localhost/puntoFrio', { useNewUrlParser: true, useUnifiedTopology: true, useCreateIndex: true, useFindAndModify: false }, (err) => {
        if (err) {
            console.log("Error conectandose a la base de datos\n");
            
        } else {
            
            console.log("Base de datos online\n");
        }
 });


const login = mongoose.model('login',{
    user: {
        type: String
    },
    password: {
        type: String
    }
}, 'login');

const newLogin = new login({user, password});

newLogin.save()
	.then((data)=>{
		
		console.log(data);
	});


/*login.find({}).exec((err, data)=>console.log(data));*/
