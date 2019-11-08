var op = ["*", ""];

for (i = 1000; i < 10000; i++) {
  var num = String(i);
  for (a = 0; a < op.length; a++) {
    for (b = 0; b < op.length; b++) {
      for (c = 0; c < op.length; c++) {
        var test =
          num.charAt(3) +
          op[a] +
          num.charAt(2) +
          op[b] +
          num.charAt(1) +
          op[c] +
          num.charAt(0);

        if (test.length > 4) {
          if (i == eval(test)) {
            console.log(i, "=", test);
          }
        }
      }
    }
  }
}
