import mongoose from "mongoose";
export const connectDb = async () => {
  try {
    mongoose.connect("mongodb://localhost:27017/farmdb");
    console.log("Connected to MongoDB");
  } catch (error) {
    console.error("Error connecting to MongoDB: ", error);
  }
};
