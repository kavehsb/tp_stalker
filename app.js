function submitToAPI(e) {
    e.preventDefault();

    const phoneVal = document.getElementById("phone-input").value;
    const topics = document.getElementById("topic-select");
    let topicVal;
    for (let i = 0; i < topics.length; i++)
    {
        if (topics[i].checked)
        {
            topicVal = topics[i].value;
            break;
        }
    }
    const tel_regex = /[0-9]{10}/;
    if (tel_regex.test(phoneVal)) {
        var full_phone = '+1';
        full_phone += phoneVal;
        let data = {
            number: full_phone,
            topic: topicVal
        };
        $.ajax({
            type: "POST",
            url: "https://djjqpcoffj.execute-api.us-west-2.amazonaws.com/prod/",
            dataType: "json",
            crossDomain: true,
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(data),

            success: function () {
                // clear form and show a success message
                alert("Success!");
                resetFields();
            },
            error: function () {
                // show an error message
                alert("Unsuccessful");
                resetFields();
            }
        });
    } else {
        alert("Please enter a valid mobile number");
        resetFields();
    }
}

function resetFields() {
    document.getElementById("phone-input").value = "";
    document.getElementById("topic-select").reset();
    location.reload();
}