const express = require('express');
const app = express();
const port = 3000;
const bodyParser = require('body-parser');
const readline = require('readline');
const axios = require('axios');

app.use(bodyParser.json());
app.use(function(req, res, next) {

	//to allow cross domain requests to send cookie information.
	res.header('Access-Control-Allow-Credentials', true);

	// origin can not be '*' when crendentials are enabled. so need to set it to the request origin
	res.header('Access-Control-Allow-Origin',  req.headers.origin);

	// list of methods that are supported by the server
	res.header('Access-Control-Allow-Methods','OPTIONS,GET,PUT,POST,DELETE');

	res.header('Access-Control-Allow-Headers', 'X-Requested-With, X-HTTP-Method-Override, Content-Type, Accept, X-XSRF-TOKEN');

	next();
});

let nodesAvailable = {};

app.get('/', (req, res) => {
	res.send('Hello World!');
});

app.listen(port, () => {
	console.log(`Example app listening at http://localhost:${port}`);
});

app.post('/assign-node', (req, res) => {
	const { body: { ip }} = req;

	if (ip && ip.length > 0) {
		if (!nodesAvailable[ip]) {
			nodesAvailable[ip] = {
				status: true,
				load: 0
			}
		}

		res.send({
			status: true,
			message: "successfully assigned child with address: " + ip
		});
	} else {
		res.send({
			status: false,
			message: 'failed to assign address'
		});

	}
});

function checkNodesStatus() {
	for (const [key, value] of Object.entries(nodesAvailable)) {

		axios.get('http://' + key + ':3001/status').then(function (response) {
			console.log(response.data);
		}).catch(function (error) {
			delete nodesAvailable[key];
			console.warn('Alert: node' + key + ' dropped');
		});
	}
}

function main() {
	setInterval(checkNodesStatus.bind(this), 3000);
}

main();












