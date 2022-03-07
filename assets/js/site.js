$(function () {
    $('.mask-date').inputmask('99/99/9999');
    $('.mask-cep').inputmask('99999-999');
    $('.mask-cpf').inputmask({ mask: "999.999.999-99", removeMaskOnSubmit: true });
    $('.mask-money').inputmask("currency", { prefix: "R$ ", radixPoint: ",", groupSeparator: ".", removeMaskOnSubmit: true });

    // $("form[id$='_form']").submit(function () {
    //     $("[class^=mask-]:not(.no-unmask").unmask();
    // })

    $('#select-variation').change(function () {
        var price = $(this).find(':selected').data('price');
        var promo_price = $(this).find(':selected').data('promotional-price');

        if (promo_price) {
            $('#var-effective-price').val(promo_price);
            $('#var-scratched-price').val(price).show()
        }
        else {
            $('#var-effective-price').val(price)
            $('#var-scratched-price').val(0).hide()
        }
    })
});
