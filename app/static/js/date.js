MktoForms2.Modernizr.inputtypes.date = false;
MktoForms2.$("body").on("mkto_date_polyfilled", function(e) {
   MktoForms2.whenReady(function(form) {
      var formEl = form.getFormElem()[0],
         dateOfBirthEl = formEl.querySelector("#DateofBirth"),
         dateOfBirthPicker = formEl.querySelector("#DateofBirth ~ .mktoDateButton");

      dateOfBirthEl.type = "text";
      dateOfBirthEl.placeholder = "Date of Birth";
      dateOfBirthPicker.style.height = MktoForms2.$(dateOfBirthEl).outerHeight() + "px";
   });
});