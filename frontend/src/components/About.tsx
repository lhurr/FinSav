import { Link } from "react-router-dom";
import { Button } from "./ui/button";

const About = () => {
  return (
    <div className="pt-20 bg-gray-50 w-full text-center text-xl">
      <div className="mt-10 text-5xl font-bold">About Us...</div>
      <div className="mt-10 ml-40 mr-40 mb-10 mx-5 p-5 bg-white shadow-md rounded-lg flex">
        <div className="flex-1 flex items-center justify-center">
          <img src="/demo1.png" alt="Demo" className="w-full h-auto" />
        </div>
        <div className="mt-5 flex flex-col flex-1 p-5 font-semibold text-justify  justify-center">
          <div className="font-bold text-2xl mb-5">FinSav - real-time smart finance assistant</div>
          <div className="text-xl mb-5">
              FinSav harnesses the power of LLMs to deliver comprehensive financial insights. Beyond answering your finance-related questions, FinSav delivers an intuitive interface to help you analyze market trends and discover the latest financial news updates. Whether you need investment advice, finance tips, or current market data, FinSav is your go-to AI assistant for accurate and timely information.
          </div>  
        </div>
        
      </div>
      <div className="mt-10 ml-40 mr-40 mb-10 mx-5 p-5 bg-white shadow-md rounded-lg flex">
        <div className="mt-5 flex flex-col flex-1 p-5 font-semibold text-justify justify-center">
          <div className="font-bold text-2xl mb-5">Real-Time Data Visualization</div>
          <div className="text-xl mb-5">
            On top of providing timely information, FinSav provides detailed graph visuals/plots to support your financial decisions. The platform's capabilities include tracking stock prices, market capitalization, cumulative returns, and more, ensuring you have the most up-to-date insights at your fingertips.        
          </div>
        </div>
        <div className="flex-1 flex items-center justify-cente m-5">
          <img src="/demo3.png" alt="Demo" className="w-full h-auto" />
        </div>
      </div>
      <Link to="/chat">
        <Button className='mb-5 text-xl font-semibold p-6'>Try FinSav Now!</Button>
      </Link>
      <footer>
        <div className='border mt-12 mx-40'></div>
        <div className='text-sm text-slate-400'>FinSav &copy;   2024</div>
      </footer>
    </div>
  )
}

export default About