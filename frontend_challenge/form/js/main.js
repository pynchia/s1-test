
const pop_API_URI = "https://populationbycity.com/";


const getpop_button = document.getElementById("getpop");
getpop_button.onclick = event => {
	const formEls = document.getElementsByClassName("formfield");
	const params = {
		q: document.getElementById("countrycode").value.toUpperCase(),
	};

	let cities = getData(pop_API_URI, params);
	console.log(cities);
	cities.then(data => {
		console.log(data);
		if (data) {
			pop_sum = 0;
			data.forEach((entry, index, array) => {
				console.log(index, entry);
				Object.entries(entry).forEach(([city, city_pop]) => {
				    console.log(`${city}: ${city_pop}`)
					pop_sum += city_pop;

				});
			})
			document.getElementById("totalpop").innerHTML = pop_sum;
		} else {
			document.getElementById("totalpop").innerHTML = `Country ${params.q} is unavailable`
		}
	});
}

// function main() {
// }

// main();
