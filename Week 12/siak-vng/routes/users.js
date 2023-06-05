const dbcon = require('../utils/database');

var express = require('express');
var router = express.Router();

function showLoginPage(err, req, res, next) {
  res.render('login', { users: '', err_msg: err});
}

router.post('/login', function(req, res, next) {
  if (req.session.isPopulated) return res.redirect('/');

  let username = req.body.username;
  let password = req.body.password;

  dbcon.query('SELECT * FROM tbl_user WHERE username = ? AND password = ?', [username, password],
    function(err, rows, fields){
      if (err) return next(err);
      if (rows.length != 1) {
        return next('Username or password not found.');
      }
      let user_id = rows[0].id;
      let user_fac = rows[0].faculty;
      req.session.user_id = user_id;
      req.session.user_fac = user_fac;
      res.redirect('/');    
    }
  );
}, showLoginPage);

router.get('/login', function(req, res, next) {
  if (req.session.isPopulated) return res.redirect('/');
  showLoginPage('', req, res, next);
});

function showRegisterPage(err, req, res, next) {
  res.render('register', { users: '', err_msg: err});
}

router.get('/register', function(req, res, next) {
  if (req.session.isPopulated) return res.redirect('/');
  showRegisterPage('', req, res, next);
});

router.post('/register', function(req, res, next) {
  if (req.session.isPopulated) return res.redirect('/');

  let username = req.body.username;
  let password1 = req.body.password;
  let password2 = req.body.password_validation;
  let faculty = req.body.faculty;

  if (password1 != password2) return next('Password mismatch.');

  dbcon.query('INSERT INTO tbl_user(username, password, faculty) VALUES(?, ?, ?)', [username, password1, faculty],
    function(err, rows, fields){
      if (err) {
        if (err.code == 'ER_DUP_ENTRY') return next('Username is not available. Please choose another username.');
        return next('Something went wrong.')
      }
      return res.redirect('/login');    
    }
  );

}, showRegisterPage);

router.get('/logout', function(req, res, next) {
  req.session = null;
  res.redirect("/login");
});

module.exports = router;
