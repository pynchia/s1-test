
async function getData(uri, params) {
    // console.log(`GET ${uri} ${params}`);

    // function formatParams() {
    //     const formatted = new URLSearchParams(params).toString();
    //     return "?"+formatted;
    // }

    // const response = await fetch(uri+formatParams());
    // if (response.ok) { // HTTP-status is 200-299
    //     try {
    //         return await response.json();
    //     } catch(e) {
    //         console.log(`Error: HTTP GET ${uri} malformed JSON in response`, e);
    //     }
    // } else {
    //     console.log(`Error: HTTP GET ${uri} response status ${response.status}`);
    // }


    // Mock the API
    mock_data = {
        "IT": [{"Turin":1000000}, {"Milan":5000000}, {"Florence":500000}],
        "NL": [{"Amsterdam":700000}, {"Rotterdam":600000}, {"The Hague":500000}],
        "UK": [{"London":3000000}, {"Oxford":5000}, {"Dover":1000}],
    };
    return mock_data[params.q]
}
