import app from "./app.js";
import { connectDb } from "./db.js";
connectDb();
app.listen(4000);
console.log("Server is running on http://localhost:4000");
