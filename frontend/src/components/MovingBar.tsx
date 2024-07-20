import { Button } from "./ui/button";

interface MovingBarProps {
  questions: string[];
}

const MovingBar:React.FC<MovingBarProps> = ({ questions }) => {
  return (
    <div className="relative h-16 w-full overflow-hidden bg-gray-50 flex items-center">
      <style>
        {`
          @keyframes move-questions {
            from { transform: translateX(0); }
            100% { transform: translateX(-100%); }
          }
          .question {
            white-space: nowrap;
          }
          
          .questions-container {
            display: flex;
            width: 250%;
            animation: move-questions 45s linear infinite;
          }
        `}
      </style>
      <div className="questions-container">
        {questions.map((question: string) => (
          <Button className="question text-lg font-medium bg-white text-black bg-white shadow-md rounded-lg hover:bg-gray-200 mx-2">
            {question}
          </Button>
        ))}
        {questions.map((question: string) => (
          <Button className="question text-lg font-medium bg-white text-black bg-white shadow-md rounded-lg hover:bg-gray-200 mx-2">
            {question}
          </Button>
        ))}
        {questions.map((question: string) => (
          <Button className="question text-lg font-medium bg-white text-black bg-white shadow-md rounded-lg hover:bg-gray-200 mx-2">
            {question}
          </Button>
        ))}
      </div>
    </div>
  );
};

export default MovingBar;
