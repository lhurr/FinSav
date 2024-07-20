import { useState, useEffect } from "react";
import axios, { AxiosError, AxiosResponse } from 'axios';
import { Button } from "./ui/button";
import { useGoogleLogin, googleLogout, TokenResponse } from "@react-oauth/google";
import { Link } from "react-router-dom";

interface UserProfile {
  id: string;
  email: string;
  verified_email: boolean;
  name: string;
  given_name: string;
  family_name: string;
  picture: string;
  locale: string;
}

const Nav = () => {
  const [user, setUser] = useState<TokenResponse | null>(null);
  const [profile, setProfile] = useState<UserProfile | null>(null);

  const login = useGoogleLogin({
    onSuccess: (codeResponse: TokenResponse) => setUser(codeResponse),
    onError: (error) => console.log('Login Failed:', error)
  });

  useEffect(
    () => {
      if (user) {
        const userToken = user.access_token;
        axios.get(`https://www.googleapis.com/oauth2/v1/userinfo?access_token=${userToken}`, {
          headers: {
            Authorization: `Bearer ${userToken}`,
            Accept: 'application/json'
          }
        }).then((res: AxiosResponse<UserProfile>) => {
          setProfile(res.data);
        }).catch((err: AxiosError) => console.log(err));
    }
  }, [user]);

  const logout = () => {
    googleLogout();
    setProfile(null);
    setUser(null);
  };

  return (
    <div className='flex flex-row justify-between w-full items-center fixed bg-white border-gray border-b-2 pr-2 pl-2'>
      <div><img src="/logo.png" alt="Logo" /></div>
      <div className="flex flex-row font-semibold pl-20">
        <Link to="/"><button className="text-xl pl-5 pr-5 p-4 transition duration-500 ease-in-out hover:bg-gray-200 hover:font-bold">Home</button></Link>
        <Link to="/about"><button className="text-xl pl-5 pr-5 p-4 transition duration-500 ease-in-out hover:bg-gray-200 hover:font-bold">About Us</button></Link>
        <Link to="/chat"><button className="text-xl pl-5 pr-5 p-4 transition duration-500 ease-in-out hover:bg-gray-200 hover:font-bold">FinSav Assistant</button></Link>
      </div>
      {user ? 
      (<div className="flex items-center justify-between px-3 py-1">
        <div className="flex items-center space-x-2">
          <img className="rounded-full" width={36} height={36} src={profile?.picture} alt="User Profile" />
          <p className="text-gray-800 font-bold">{profile?.name}</p>
        </div>
        <Button onClick={logout} className="ml-4">Log out</Button>
      </div>) : 
      (<Button onClick={() => login()}>Sign in with Google</Button>)}
    </div>
  )
}

export default Nav;