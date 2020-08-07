 $(document).on('click','.deleteRecord',function () {
        var id = $(this).attr('rel');
        var deleteFunction = $(this).attr('rel1');
//         alert(id);
//         alert(deleteFunction);
//         return false;
        Swal.fire({
            title: "Are you sure?",
            text: "You won't be able to recover deleted data !!",
            icon: "error",
            showCancelButton: true,
            confirmButtonColor: "#d33",
            cancelButtonColor: "#000",
            confirmButtonText: "Yes, delete it!"
        }).then(result => {
            if (result.value) {
                window.location.href =  deleteFunction + "/" + id;
//                $.ajax({
//                type: 'GET',
//                data: {'id': id},
//                url: '/delete-user/',
//                success:function (response) {
//                            $('#datatables').DataTable().ajax.reload();
//                            if(response =='True'){
//                                swal.fire({
//                                title: "Deleted Successfully",
//                                    text: "You won't be able to recover deleted data !!",
//                                    icon: "success",
//
//                                });
//                            }
//                        }
//
//                })
            }
        });
    });

$(document).ready(function () {
    $('#id_start_date').datetimepicker({
        format: 'Y-m-d H:i:s'
    });
    $('#id_end_date').datetimepicker({
        format: 'Y-m-d H:i:s'
    });
    $('#id_reminder_date').datetimepicker({
        format: 'Y-m-d H:i:s'
    });
    $('#start_date').datetimepicker({
        format: 'Y-m-d H:i:s'
    });
});




