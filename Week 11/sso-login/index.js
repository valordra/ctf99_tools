var express = require('express');
var router = express.Router();
var jws = require('jws');
var {SECRET_KEY, ADMIN, FLAG} = require('../utils/secret'); 

function getJWTTokenFromHeaderOrCookie(req) {
  if (req.headers.authorization && req.headers.authorization.split(' ')[0] === 'Bearer') {
    return req.headers.authorization.split(' ')[1];
  } else if (req.cookies && req.cookies.jwt) {
    return req.cookies.jwt;
  }
  return null;
}

function jwtMiddleware(req, res, next) {
  let token = getJWTTokenFromHeaderOrCookie(req);
  let payload = jws.decode(token, {complete: true});
  let header = payload.header;
  let valid;
  try {
    valid = jws.verify(token, header.alg, SECRET_KEY);
  } catch (e) {
    return next(e);
  }
  if (!valid) return next('invalid token');

  req.user = payload.payload;
  return next();
}

router.get('/verify', jwtMiddleware, function(req, res, next) {
  res.send({status: 'ok', msg: `welcome ${req.user.username}!`});
});

router.get('/admin', jwtMiddleware, function(req, res, next) {
  if (!req.user.isAdmin) return res.sendStatus(403);
  res.send({status: 'ok', msg: FLAG});
});

router.post('/token', function(req, res, next) {
  let username = req.body.username;
  let password = req.body.password;

  let jwt_header = {typ: 'JWT', alg: 'HS256'};
  let jwt_payload = {
    username: username,
    isAdmin: false
  }

  if (username === ADMIN.username) {
    if (password !== ADMIN.password) return res.sendStatus(401);
    jwt_payload.isAdmin = true;
  }

  let token = jws.sign({header: jwt_header, payload: jwt_payload, secret: SECRET_KEY})
  res.cookie('jwt', token);
  return res.send({status: 'ok', msg: 'Authenticated'});
});

router.get('/', function(req, res, next) {
  res.send({status:'ok', msg: 'Hello!'});
})

module.exports = router;
