const argv = require('arg');

let alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
let rotate = (c, s) => (alphabet.indexOf(c) + s) % alphabet.length;


function msg_generator(msg, shift){ 
    let generated_msg = '';

    for(const chr of msg){
        if(alphabet.indexOf(chr) > -1){
            // let enc = alphabet.charAt(rotate(chr, shift));
            let enc = alphabet.at(rotate(chr, shift));
            generated_msg = generated_msg.concat(enc);
        }else{
            generated_msg = generated_msg.concat(chr);
        }
    }

    return generated_msg;   
}


function toencrypt(msg, key){
    let encrypted_msg = msg_generator(msg, key);
    return encrypted_msg;
}

module.exports.toencrypt = toencrypt;

function todecrypt(msg, key){
    key = -key;
    let decrypted_msg = msg_generator(msg, key);
    return decrypted_msg;
}

module.exports.todecrypt = todecrypt;

function main(todo, msg = '', key){
    if(msg.length < 1){
        console.log('Nothing to do here. There is no message!');
    }
    try{
        if(todo == 'toencrypt'){
            let encrypted_msg = toencrypt(msg, key); 
            console.log(encrypted_msg);
        }else{
            let decrypted_msg = todecrypt(msg, key);
            console.log(decrypted_msg);
        }
    }catch(error){
        console.error(error);
    }    
}


if(require.main === module){
    const options = argv({
            '--todo': String,
            '--message': String,
            '--key': Number,
            '-t': '--todo',
            '-m': '--message',
            '-k': '--key'
    })    
    main(options['--todo'], options['--message'], options['--key']);   
}


   