function sendArticleComment(articleId) {
    // console.log('submit comment')
    var comment = $('#commentText').val()
    var parentId = $('#parent_id').val()
    console.log(comment)

    $.get('/articles/add-article-comment',
        {
            comment,
            articleId,
            parentId: parentId
        }).then(res => {
        $('#comments_area').html(res)
        $('#commentText').val('')
        $('#parent_id').val('')
        if (parentId !== null && parentId !== '') {
            document.getElementById('single_comment_box_' + parentId).scrollIntoView({behavior: 'smooth'})
        } else {
            document.getElementById('comments_area').scrollIntoView({behavior: 'smooth'})
        }
    })
}

function fillParentId(parent_id) {
    $('#parent_id').val(parent_id)
    document.getElementById('comment_form').scrollIntoView({behavior: 'smooth'})
}


function filterProducts() {
    const filter_price = $("#sl2").val();
    const start_price = filter_price.split(',')[0];
    const end_price = filter_price.split(',')[1];
    $("#start_price").val(start_price);
    $("#end_price").val(end_price);
    $("#filter_form").submit();
}

function fillPage(page) {
    $("#page").val(page);
    $("#filter_form").submit();
}

function showLargeImage(imageSrc) {
    $('#main_image').prop('src', imageSrc);
    $('#show_large_image_modal').prop('href', imageSrc);
}

function addProductToOrder(productId) {
    const product_count = $('#product_count').val()
    $.get('/order/add-to-order?product_id=' + productId + '&count=' + product_count).then(res => {
        Swal.fire({
            title: 'اعلان',
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: '#3085d6',
            confirmButtonText: res.confirmButtonText
        }).then((result) => {

            if (result.isConfirmed && res.status === 'not_auth' ) {
                window.location.href = '/login'

            }
        })

    })
}


function removeOrderDetail(detailId) {
    $.get('/user/remove-order-detail?detail_id=' + detailId).then(res=> {
        if(res.status === 'success'){
            $('#order-detail-content').html(res.body)
        }
    })
}

function changeOrderDetailCount(detailId,state){
    $.get('/user/change-order-detail?detail_id=' + detailId + '&state=' + state).then(res=> {
        if(res.status === 'success'){
            $('#order-detail-content').html(res.body)
        }
    })
}