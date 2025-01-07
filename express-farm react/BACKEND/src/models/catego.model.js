import mongoose from "mongoose";

const categoSchema=new mongoose.Schema({
    name:{
        type:String,
        required:true,
        unique: true,
        trim: true
    }, 
    description:{
        type:String,
        required:true,
    },
   
      
},
{
timestamps:true
}
)

export default mongoose.model('Catego',categoSchema)