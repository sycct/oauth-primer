import express, { json } from "express";
import dotenv from "dotenv";

dotenv.config()

const app = express();
app.use(json());

const port = process.env.PORT;

app.listen(port, () => {
  console.log(`[server]:server is running on port http://localhost:${port}`);
});
