import express from "express";
import morgan from "morgan";
import cors from "cors";
import cookieParser from "cookie-parser";
import authRoutes from './routes/auth.routes.js';
import categoRoutes from './routes/catego.routes.js';
import medicRoutes from './routes/medic.routes.js';
const app = express();
app.use(cors({
    credentials:true,
    origin:'http://localhost:3000'
}))

app.use(morgan("dev"));
app.use(express.json());
app.use(cookieParser());
app.use('/api',authRoutes);
app.use('/api',categoRoutes);
app.use('/api',medicRoutes);
export default app;
