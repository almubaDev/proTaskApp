$(document).ready(_ => {

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
            $('.task_card').hide(500);
            $('.task_card:contains("Completada")').show(500);
        });

    $('.filt_exp').click(_ => {
            $('.task_card').hide(500);
            $('.task_card:contains("Expirada")').show(500);
        });

        $('.filter_tag_button').click(_ => {
            event.preventDefault(); 

            let tag = $('#search_tag').val().toLowerCase(); 
            $('.task_card').hide(500);

            $(`.task_card`).filter((index, element)=> {
                return $(element).text().toLowerCase().includes(tag);
            }).show(500);
            
        });
    
    

    var today = new Date().toISOString().split('T')[0];
    $("#fecha").attr("min", today);
});


