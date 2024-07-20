import { useEffect } from "react";
import { sessionState, useChatSession } from "@chainlit/react-client";
import { Playground } from "./components/playground";
import { useRecoilValue } from "recoil";
import {
  createBrowserRouter,
  RouterProvider
} from "react-router-dom";
import Layout from "./components/Layout";
import Home from "./components/Home";
import About from "./components/About";
import MissingPage from "./components/MissingPage";

const userEnv = {};

const router = createBrowserRouter([
  {
    element: <Layout />, 
    children: [
      {
        path: 'chat',
        element: <Playground />,
      },
      {
        path: '/',
        element: <Home />,
      },
      {
        path: 'home',
        element: <Home />,
      },
      {
        path: 'about',
        element: <About />
      },
      {
        path: '*',
        element: <MissingPage />
      }
    ]
  }
]);

function App() {
  const { connect } = useChatSession();
  const session = useRecoilValue(sessionState);
  useEffect(() => {
    if (session?.socket.connected) {
      return;
    }
    fetch("http://localhost:3002/custom-auth")
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        connect({
          userEnv,
          accessToken: `Bearer: ${data.token}`,
        });
      });
  }, [connect]);

  return (
    <RouterProvider router={router}/>
  );
}

export default App;
