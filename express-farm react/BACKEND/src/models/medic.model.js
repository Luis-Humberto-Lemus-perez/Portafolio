import mongoose from "mongoose";

const medicSchema=new mongoose.Schema({
    name:{
        type:String,
        required:true,
    }, 
    description:{
        type:String,
        required:true,
    },
    img:{
        type:String,
        required:true
    },
    precio:{
        type:Number,
        required:true
    },
    stock:{
        type:Number,
        required:true
    },

    category:{
        type:mongoose.Schema.Types.ObjectId,
        ref:'Category',
        required:true
    }


},
{
timestamps:true
}
)

export default mongoose.model('Medic',medicSchema)