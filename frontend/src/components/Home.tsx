import { Link } from 'react-router-dom';
import { Button } from './ui/button'; 
import MovingBar from './MovingBar';

const HomePage = () => {
  const questions = [
    [
      "What is the stock market?",
      "How to invest in real estate?",
      "What are mutual funds?",
      "How to save for retirement?",
      "What is cryptocurrency?",
      "How to create a budget?",
      "What is an ETF?",
      "How to improve credit score?",
    ],
    [
      'Tell me more about NVIDIA!',
      'Should I invest in GME?',
      'Tell me about Google price vol chart',
      'Give me a financial summary of amazon',
      "What is the current price of Tesla shares?",
      "Tell me performance of Meta and Google stocks",
      "Tell me about the latest dividend yield for JPMorgan Chase."
    ]
  ];

  return (
    <div className="pt-20 bg-gray-50 w-full text-center text-xl">
      <div className="mt-10 text-5xl font-bold">Welcome to FinSav!</div>
      <div className="mt-5 mb-5">
        Get up-to-date information about the realm of finance!
      </div>
      <div className="mt-10 ml-40 mr-40 mb-10 mx-5 p-5 bg-white shadow-md rounded-lg">
        <h2 className="text-3xl font-semibold mb-5">What is FinSav?</h2>
        <p className="text-lg mb-5">
          FinSav is a cutting-edge <i>real-time</i> smart finance assistant powered by advanced language models designed to provide insights to all your finance-related questions. Whether you're looking for up-to-date market trends, investment advice, or financial planning tips, FinSav is here to help.
        </p>
      </div>
      <Link to="chat">
        <Button className='mb-5 text-xl font-semibold p-6'>Try FinSav!</Button>
      </Link>
      <MovingBar questions={questions[0]}/>
      <MovingBar questions={questions[1]}/>
      <footer className='bg-gray-50'>
        <div className='border mt-20 mx-40'></div>
        <div className='text-sm text-slate-400'>FinSav &copy;   2024</div>
      </footer>
    </div>
  );
};

export default HomePage;
