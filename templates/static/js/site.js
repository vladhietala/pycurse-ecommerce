$(function () {
    $('.mask-date').mask('00/00/0000');
    $('.mask-cep').mask('00000-000');
    $('.mask-cpf').mask("000.000.000-00");

    $("form[id$='_form']").submit(function () {
        $("[class^=mask-]:not(.no-unmask").unmask();
    })
});
