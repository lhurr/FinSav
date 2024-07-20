import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.tsx";
import { RecoilRoot } from "recoil";
import "./index.css";
import { ChainlitAPI, ChainlitContext } from "@chainlit/react-client";
import { GoogleOAuthProvider } from "@react-oauth/google";

const CHAINLIT_SERVER = "http://localhost:3002/chainlit";

const apiClient = new ChainlitAPI(CHAINLIT_SERVER, "webapp");
const GOOGLE_CLIENT_ID = import.meta.env.VITE_GOOGLE_CLIENT_ID;

ReactDOM.createRoot(document.getElementById("root")!).render(
    <React.StrictMode>  
      <GoogleOAuthProvider clientId={GOOGLE_CLIENT_ID}>
        <ChainlitContext.Provider value={apiClient}>
          <RecoilRoot>
            <App />
          </RecoilRoot>
        </ChainlitContext.Provider>   
      </GoogleOAuthProvider>
    </React.StrictMode>
);
