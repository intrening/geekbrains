<font size="7">
    <div class="webinar-date">
        <div class="webinar-date-s"></div>
    </div>
</font>

<script>
  (function (doc) {
          var t = (new Date()).getTime() + 3600000 * 3;
          var d1 = new Date(t);
          var dm = new Date(d1.getUTCFullYear(), d1.getUTCMonth(), d1.getUTCDate(), d1.getUTCHours(), d1.getUTCMinutes(), d1.getUTCSeconds());
          var h = dm.getHours(),
              sh = 0;

          var min = dm.getMinutes();
          if (h >= 21) {
              sh = 24 + 11;
          } else if (h < 11) {
              sh = 11;
          } else {
              sh = h + 1;
          }
          var dw = new Date(dm.getFullYear(), dm.getMonth(), dm.getDate());
          t = dw.getTime() + sh * 3600000;
          dw = new Date(t);

          var day = dw.getDate();
          var hour = dw.getHours();
          var months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'];
          var month = months[dw.getMonth()];

          var s = 'Начало в ' + hour + ':00 МСК';

          var a = doc.querySelectorAll('.webinar-date-s');
          for (var i = 0; i < a.length; i++) {
              a[i].innerHTML = s;
          }

  })(document);
</script>