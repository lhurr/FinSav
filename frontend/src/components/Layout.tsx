import { Outlet } from 'react-router-dom';
import Nav from './Nav';

const Layout = () => {
  return (
    <div className="flex flex-col h-screen">
      <Nav />
      <Outlet />
    </div>
  );
};

export default Layout;