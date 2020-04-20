var predBtn = document.getElementById('predict')

function handlePrediction(){

    $.ajax({
        url:'',
        method: 'POST',
        data : {

        },
        headers: {
            "X-CSRFToken": csrftoken
        }
    })
        .done(function(response){
            console.log("Prediction complete");
            if (response.success){
                window.location.href = 'azure/home.html';
            } else {
                window.location.href = 'azure/error.html';
            }
        })
        .fail(function(error){
            console.log(error);
        });
}

predBtn.addEventListener('click', function(e){
    e.preventDefault();

    var predictionPayload = {
        fun: '', 
        callback: handlePrediction
    };
    
})

predBtn.addEventListener('click', function(f){
    $.ajax({
        url:'/predict/',
        method: 'POST',
        data : {
            probability: prob,
            prediction_result : pred_result
        },
        headers: {
            "X-CSRFToken": csrftoken
        }
    })
        .done(function(response){
            console.log(response);
            if (response.success){
                window.location.href = 'azure/home.html';
            } else {
                window.location.href = 'azure/error.html';
            }
        })
        .fail(function(error){
            console.log(error);
        });
})