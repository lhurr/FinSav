import { Link } from "react-router-dom";
import { Button } from "./ui/button";

const MissingPage = () => {
  return (
    <div className="flex flex-col items-center justify-center bg-gray-50 min-h-screen w-full text-center text-xl">
      <div className="text-3xl font-bold content-center flex">404   <span className="ml-5 text-2xl font-light">| This page could not be found.</span></div>
      <Link to="/">
        <Button className="mt-5">Back to home page</Button>
      </Link>
    </div>
  )
}

export default MissingPage