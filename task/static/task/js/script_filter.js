$(document).ready(_ => {
    //Filtro de pendientes
    $('.filt_all').click(_ => {
        $('.task_card').show(500);
    });
    $('.filt_pend').click(_ => {
        $('.task_card').hide(500);
        $('.task_card:contains("Pendiente")').show(500);
    });

    $('.filt_in_proc').click(_ => {
        //Filtro completadas
            $('.task_card').hide(500);
            $('.task_card:contains("En progreso")').show(500);
        });

    $('.filt_comp').click(_ => {
        //Filtro completadas
            $('.task_card').hide(500);
            $('.task_card:contains("Completada")').show(500);
        });

    $('.filt_exp').click(_ => {
        //Filtro completadas
            $('.task_card').hide(500);
            $('.task_card:contains("Expirada")').show(500);
        });

        var today = new Date().toISOString().split('T')[0];
    $("#fecha").attr("min", today);
});


