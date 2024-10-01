const cipher = require ('./cipher.cjs');

var assert = require('assert');

describe('cipher', function() {
    describe('#todecrypt', function(){
        it('should return the original alphabet', function(){
            s = Math.floor(Math.random() * 100) + 1;
            a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

            enc = cipher.toencrypt(a, s);
            dec = cipher.todecrypt(enc, s);

            assert.equal(a, dec);
        });
    });
})
