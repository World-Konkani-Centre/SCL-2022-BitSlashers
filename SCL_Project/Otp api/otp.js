import mongoose from "mongoose";

const userSchema=new mongoose.Schema({
   number:{
        type:Number,
        required:true
    },
  otp :{ 
      type:Number,
      required:true
  },
});
const User =mongoose.model("user",userSchema);
export default User;