"use strict";

const serverless = require("serverless-http");
const express = require("express");
const app = express();
const AWS = require("aws-sdk");
const bodyParser = require("body-parser");

const dynamoDB = new AWS.DynamoDB.DocumentClient();
const USERS_TABLE = process.env.USERS_TABLE;
// Recuperar la info via POST
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", (req, res) => {
	res.send("Hola mundo desde express");
});

app.post("/users", (req, res) => {
	const { userId, name } = req.body;
	const params = {
		TableName: USERS_TABLE,
		Item: {
			userId,
			name,
		},
	};
	dynamoDB.put(params, (error) => {
		if (error) {
			console.log(error);
			res.status(400).json({
				error: "No se pudo crear el usuario",
			});
		} else {
			res.json({ userId, name });
		}
	});
});

app.get("/users", (req, res) => {
	const params = {
		TableName: USERS_TABLE,
	};
	dynamoDB.scan(params, (error, result) => {
		if (error) {
			console.log(error);
			res.status(400).json({
				error: "No se pudo acceder a los usuarios.",
			});
		} else {
			const { Items } = result;
			res.json({
				success: true,
				message: "Usuarios cargados correctamente.",
				users: Items,
			});
		}
	});
});

app.get("/user/:userId", (req, res) => {
	const params = {
		TableName: USERS_TABLE,
		Key: {
			userId: req.params.userId,
		},
	};
	dynamoDB.get(params, (error, result) => {
		if (error) {
			console.log(error);
			return res.status(400).json({
				error: "No se pudo acceder al usuario.",
			});
		}
		if (result.Item) {
			const {userId, name} = result.Item;
			return res.json({ userId, name });
		} else {
			res.status(404).json({ error: "Usuario no encontrado" });
		}
	});
});

module.exports.generic = serverless(app);
