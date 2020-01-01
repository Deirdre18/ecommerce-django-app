//js code required by stripe api, using jquery. Links up  html and django forms to stripe's api (in js).

$(function() {
  $("#payment-form").submit(function() {
    var form = this;
    var card = {
      //just referring to id's
      number: $("#id_credit_card_number").val(),
      expMonth: $("#id_expiry_month").val(),
      expYear: $("#id_expiry_year").val(),
      cvc: $("#id_cvv").val()
    };
    // link to strip for developers for more info - https://stripe.dev/
    Stripe.createToken(card, function(status, response) {
      if (status === 200) {
        // very important to hide these details. They should never be shown, as stripe handle all payments.
        $("#credit-card-errors").hide();
        $("#id_stripe_id").val(response.id);

        // Prevent the credit card details from being submitted
        // to our server
        $("#id_credit_card_number").removeAttr('name');
        $("#id_cvv").removeAttr('name');
        $("#id_expiry_month").removeAttr('name');
        $("#id_expiry_year").removeAttr('name');

        form.submit();
        // if there is no '200' error, stripe will send error message
      } else {
        // from stripe api. Error message in div in checkout.html
        // all these id's are from stripe's developers site, can't just write whatever you want. This is trequired for stripe api to work
        $("#stripe-error-message").text(response.error.message);
        $("#credit-card-errors").show();
        $("#validate_card_btn").attr("disabled", false);
      }
    });
    return false;
  });
});