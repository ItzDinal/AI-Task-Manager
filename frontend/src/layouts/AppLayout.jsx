import { Outlet } from "react-router-dom";
import Sidebar from "../components/sidebar/Sidebar.jsx";
import TopNavbar from "../components/navbar/TopNavbar.jsx";

// Scalable app shell that composes navigation and route content.
function AppLayout() {
  return (
    <div className="min-h-screen w-full">
      <TopNavbar />
      <div className="flex w-full">
        <Sidebar />
        <main className="flex-1">
          <Outlet />
        </main>
      </div>
    </div>
  );
}

export default AppLayout;
