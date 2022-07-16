import express from "express"
import path from "path"
import mongoose from "mongoose"
import cors from "cors"
import dotenv from "dotenv"
import User from "./otp.js"
// import axios from "axios"

const __dirname=path.resolve()

dotenv.config({path:__dirname+"/.env"});
const app=express()
const url=process.env.DATABASE_URL
mongoose
    .connect(url,
        { useNewUrlParser: true,
             useUnifiedTopology: true
        })
    .then(() => console.log("Database Connected Successfully"))
    .catch(err => console.log(err));
const corsOptions ={
   origin:'*', 
   credentials:true,            //access-control-allow-credentials:true
   optionSuccessStatus:200,
}
app.use(cors(corsOptions))
app.use(express.json())
app.use(express.urlencoded({extended:true}))

app.post("/send",async(req,res)=>{
    const otp=Math.floor(100000 + Math.random() * 900000);
    const number=req.body.number
    let user=await User.findOne({number:number});
    if(!user){
    user=new User({
        number:number,
        otp:otp
    });
}
user.otp=otp
await user.save();
// const encodedParams = new URLSearchParams();
// encodedParams.append("to", "+91"+number);
// encodedParams.append("p",process.env.API_KEY);
// encodedParams.append("text", otp+" is your OTP");

// const options = {
//   method: 'POST',
//   url: 'https://sms77io.p.rapidapi.com/sms',
//   headers: {
//     'content-type': 'application/x-www-form-urlencoded',
//     'X-RapidAPI-Key': process.env.X_RapidAPI_Key,
//     'X-RapidAPI-Host': 'sms77io.p.rapidapi.com'
//   },
//   data: encodedParams
// };

// axios.request(options).then(function (response) {
// 	console.log(response.data);
// }).catch(function (error) {
// 	console.error(error);
// });
console.log(otp)
   return res.status(200).json({Msg:"Msg Sent",otp:otp})
})
app.post("/verify",async(req,res)=>{
    const number=req.body.number;
    const otp=req.body.otp;
    const user=await User.findOne({number:number});
    if(!user)
        return res.status(200).json({Msg:"Invalid Request"});
    if(user.otp==otp){
       await User.deleteOne({number:number});
        return res.status(200).json({Msg:"Success"})
    }
    else
    return res.status(200).json({Msg:"Failure"});
})
const PORT = process.env.PORT || 8081;
app.listen(PORT, console.log(`Server started on port ${PORT}`));