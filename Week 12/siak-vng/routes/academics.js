const dbcon = require('../utils/database');

var express = require('express');
var router = express.Router();

router.get('/class', function(req, res, next) {
  if (!req.session.isPopulated) return res.redirect('/login');

  let sql = `SELECT * FROM tbl_class WHERE faculty = '${req.session.user_fac}'`;
  dbcon.query(sql, 
    function(err, rows, fields){
      if (err) return next("Something went wrong.");
      return res.render('class_list', {'classes': rows, 'users': req.session.user_id});
    }
  )
});

module.exports = router;
